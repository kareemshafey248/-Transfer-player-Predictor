# Transfer Intelligence Engine — AI Prediction Model
# Simulates a trained ML model using a weighted scoring approach

from transfer_data import LEAGUE_DIFFICULTY

def calculate_transfer_score(age, fee, from_league, to_league, goals, assists, minutes, role):
    """
    Calculates a Transfer Success Score (0-100) based on player profile.
    Higher = More likely to succeed.
    Returns dict with score, risk level, recommendation, and factor breakdown.
    """
    score = 0
    factors = {}

    # ── 1. Age Factor (peak window is 23-27) ─────────────────────
    if 23 <= age <= 27:
        age_score = 35
    elif 21 <= age <= 29:
        age_score = 25
    elif age < 21:
        age_score = 18   # Young talent — high ceiling, uncertain
    else:
        age_score = 10   # Veteran — declining trajectory
    factors["Age Factor"] = age_score
    score += age_score

    # ── 2. Fee Efficiency (value for money) ──────────────────────
    # Estimate expected output score based on goals+assists per 90
    if minutes > 0:
        raw_output_per90 = ((goals + assists) / minutes) * 90
    else:
        raw_output_per90 = 0
        
    # Adjust output by origin league difficulty (harder league = more valuable stats)
    from_diff = LEAGUE_DIFFICULTY.get(from_league, 6.0)
    to_diff = LEAGUE_DIFFICULTY.get(to_league, 8.0)
    
    output_per90 = raw_output_per90 * (from_diff / 8.0) # Normalized to Bundesliga level

    
    expected_fee_threshold = output_per90 * 12  # rough fair value in €M
    
    if role in ["Defender", "GK"]:
        expected_fee_threshold = 40  # defenders rarely score
        fee_score = max(0.0, 25.0 - (max(0.0, float(fee) - expected_fee_threshold) * 0.2))
    else:
        fee_score = max(0.0, 25.0 - (max(0.0, float(fee) - expected_fee_threshold) * 0.15))
    
    fee_score = round(min(fee_score, 25), 1)
    factors["Fee Efficiency"] = fee_score
    score += fee_score

    # ── 3. League Leap Difficulty ─────────────────────────────────
    leap = to_diff - from_diff

    # Dynamic adaptation scoring based on the leap
    if leap <= -3.0:     # Huge step down (e.g., PL to Saudi) -> Guaranteed adaptation
        leap_score = 25  # Bonus points for massive difficulty drop
    elif leap <= -1.0:   # Moderate step down (e.g., PL to Ligue 1)
        leap_score = 20
    elif leap <= 0.5:    # Similar level (e.g., La Liga to PL) -> Manageable risk
        leap_score = 15
    elif leap <= 2.0:    # Step up (e.g., Eredivisie to PL) -> High risk
        leap_score = 10
    else:                # Huge leap (e.g., MLS to PL) -> Extreme risk
        leap_score = 5

    
    factors["Adaptation Risk"] = leap_score
    score += leap_score

    # ── 4. Performance History Score ─────────────────────────────
    if role in ["Defender", "GK"]:
        perf_score = 20 if minutes >= 2500 else 12
    else:
        if output_per90 >= 1.0:
            perf_score = 20
        elif output_per90 >= 0.6:
            perf_score = 15
        elif output_per90 >= 0.3:
            perf_score = 10
        else:
            perf_score = 5
    factors["Performance History"] = perf_score
    score += perf_score

    # ── Final Score Normalization ─────────────────────────────────
    final_score = round(min(max(score, 5), 100), 1)

    # ── Risk Level ───────────────────────────────────────────────
    if final_score >= 75:
        risk = "Low Risk"
        risk_color = "#10b981"
        recommendation = "🟢 Strong Buy — This profile checks all boxes. High probability of success."
    elif final_score >= 50:
        risk = "Medium Risk"
        risk_color = "#f5a623"
        recommendation = "🟡 Conditional Buy — Solid profile but has some risk factors. Scout carefully."
    else:
        risk = "High Risk"
        risk_color = "#ef4444"
        recommendation = "🔴 Avoid — High risk of underperformance. Consider alternative targets."

    return {
        "score": final_score,
        "risk": risk,
        "risk_color": risk_color,
        "recommendation": recommendation,
        "factors": factors,
        "output_per90": round(raw_output_per90, 2)
    }


def get_league_stats(transfers):
    """
    Analyzes which leagues produce the best success rates.
    """
    stats = {}
    for t in transfers:
        league = t["to_league"]
        if league not in stats:
            stats[league] = {"total": 0, "success": 0, "partial": 0, "flop": 0}
        stats[league]["total"] += 1
        if t["result"] == "Success":
            stats[league]["success"] += 1
        elif t["result"] == "Partial":
            stats[league]["partial"] += 1
        else:
            stats[league]["flop"] += 1
    
    return {
        k: {
            **v,
            "success_rate": round((v["success"] / v["total"]) * 100, 1) if v["total"] > 0 else 0
        }
        for k, v in stats.items() if v["total"] >= 2
    }
