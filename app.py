import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from transfer_engine import calculate_transfer_score, get_league_stats
from transfer_data import TRANSFERS, BEST_TRANSFERS, WORST_TRANSFERS, LEAGUE_DIFFICULTY, PLAYER_DATABASE

# ── Page Config ────────────────────────────────────────────────────
st.set_page_config(
    page_title="Transfer Intelligence Engine | Kareem Elshafey",
    page_icon="🧠",
    layout="wide",
)

# ── Premium Styles (Navy Gold Theme) ─────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
    background-color: #0d1b2a;
    color: #e5e7eb;
}
.stApp { background: linear-gradient(160deg, #0d1b2a 0%, #1a2e45 100%); }
.stSidebar { background: #0a1628 !important; }

.card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    padding: 22px;
    margin-bottom: 18px;
}
.gold-border { border: 1px solid #f5a623 !important; }
.score-ring {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 160px;
    height: 160px;
    border-radius: 50%;
    background: conic-gradient(#f5a623 0%, #f5a623 var(--pct), rgba(255,255,255,0.05) var(--pct));
    margin: 0 auto 15px auto;
}
.pill {
    display: inline-block;
    padding: 4px 14px;
    border-radius: 20px;
    font-weight: 700;
    font-size: 0.8rem;
}
.pill-success { background: rgba(16,185,129,0.15); color: #10b981; border: 1px solid #10b981; }
.pill-partial  { background: rgba(245,166,35,0.15);  color: #f5a623; border: 1px solid #f5a623;  }
.pill-flop    { background: rgba(239,68,68,0.15);   color: #ef4444; border: 1px solid #ef4444;  }
.sidebar-brand { text-align:center; padding: 18px 0; border-bottom: 1px solid rgba(255,255,255,0.07); margin-bottom: 15px; }

h1, h2, h3 { font-weight: 800 !important; color: #ffffff !important; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ────────────────────────────────────────────────────────
st.sidebar.markdown("""
<div class="sidebar-brand">
    <div style="font-size:3rem;">🧠</div>
    <div style="font-size:1.3rem; font-weight:800; color:#f5a623;">TRANSFER INTELLIGENCE</div>
    <div style="font-size:0.7rem; color:#9ca3af; letter-spacing:2px;">ENGINE v1.0</div>
</div>
""", unsafe_allow_html=True)

nav = st.sidebar.radio("Navigate", [
    "🏠 Welcome Hub",
    "🔍 Transfer Predictor",
    "📜 Hall of Fame & Shame",
    "📊 League Intelligence"
])

st.sidebar.markdown("""
<div style="padding:14px; background:rgba(245,166,35,0.08); border-radius:10px; margin-top:25px; border-left:3px solid #f5a623;">
    <div style="font-weight:800; color:#fff; font-size:1rem;">Kareem Elshafey</div>
    <div style="color:#f5a623; font-size:0.8rem; font-weight:600;">Football Analyst & Data Specialist</div>
    <div style="color:#9ca3af; font-size:0.72rem; margin-top:6px;">📱 +20 112 797 3132</div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────
# 🏠 WELCOME HUB
# ─────────────────────────────────────────────────────────────────
if nav == "🏠 Welcome Hub":
    st.markdown("<h1 style='font-size:3rem;'>🧠 Transfer Intelligence Engine</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:1.2rem; color:#9ca3af;'>The AI-powered scouting tool that predicts transfer success before the deal is signed.</p>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<h2>❓ What Questions Does This Project Answer?</h2>", unsafe_allow_html=True)

    questions = [
        ("🎯", "Will this transfer be a success or a flop?",
         "For Coaches & Directors", "Our AI model scores every player profile 0-100. Input any player's age, fee, stats, and leagues — get an instant Success Prediction."),
        ("🌍", "Which leagues produce the most successful transfers?",
         "For Analysts & Scouts", "Some leagues are prove grounds, others are dead ends. We rank every league by its transfer success rate based on real data."),
        ("👤", "What player profile has the highest success rate?",
         "For Scouts", "Peak-age, efficient performers who don't over-cost consistently outperform. The data shows exactly what profile wins."),
        ("💶", "Does spending more money guarantee success?",
         "For Directors & Fans", "No. We show exactly how fee efficiency affects outcomes — and why some of history's best transfers cost under €50M."),
        ("📖", "Who were the best and worst transfers in football history?",
         "For Fans", "From Salah at €42M to Lukaku's €113M disaster — we rank them with real data and explain exactly why they succeeded or failed."),
    ]

    cols = st.columns(2)
    for i, (icon, q, audience, answer) in enumerate(questions):
        col = cols[i % 2]
        with col:
            q_html = f"""
<div class="card {'gold-border' if i == 0 else ''}">
<div style="font-size:2rem; margin-bottom:8px;">{icon}</div>
<h3 style="font-size:1.1rem; margin:0 0 5px 0;">{q}</h3>
<div style="font-size:0.75rem; color:#f5a623; font-weight:600; margin-bottom:10px;">👥 {audience}</div>
<p style="font-size:0.9rem; color:#9ca3af; margin:0;">{answer}</p>
</div>
"""
            st.markdown(q_html, unsafe_allow_html=True)

    st.markdown("""
<div class="card gold-border" style="text-align:center; margin-top:15px;">
<h3 style="color:#f5a623 !important;">💡 How the AI Engine Thinks</h3>
<p style="color:#9ca3af;">We analyze 4 key factors: <b style="color:#fff;">Age at Transfer</b> (is the player in their peak window?),
<b style="color:#fff;">Fee Efficiency</b> (is the cost justified by output?),
<b style="color:#fff;">League Leap</b> (how big is the difficulty jump?), and
<b style="color:#fff;">Performance History</b> (goals + assists per 90 mins).</p>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────
# 🔍 TRANSFER PREDICTOR
# ─────────────────────────────────────────────────────────────────
elif nav == "🔍 Transfer Predictor":
    st.markdown("<h1>🔍 Transfer Success Predictor</h1>", unsafe_allow_html=True)
    st.markdown("Select a real player from our database to auto-fill their real-world stats, or enter details manually.")

    # Player Selection
    player_options = ["— Enter Manually —"] + list(PLAYER_DATABASE.keys())
    selected_player = st.selectbox("⚡ Choose a Player (Auto-fills transfer data):", player_options)

    # Auto-fill logic based on selection
    if selected_player != "— Enter Manually —":
        p_data = PLAYER_DATABASE[selected_player]
        def_name = selected_player.split(" (")[0]
        def_age = p_data["age"]
        def_role = p_data["role"]
        def_fee = p_data["value"]
        def_goals = p_data["goals"]
        def_assists = p_data["assists"]
        def_minutes = p_data["minutes"]
        def_league = p_data["league"]
    else:
        def_name = ""
        def_age = 24
        def_role = "Forward"
        def_fee = 50
        def_goals = 15
        def_assists = 8
        def_minutes = 2700
        def_league = "Premier League"

    with st.form("predictor_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            player_name = st.text_input("Player Name", value=def_name, placeholder="e.g. Kylian Mbappé")
            age = st.slider("Player Age", 16, 38, value=def_age)
            roles = ["Forward", "Winger", "Midfielder", "Defender", "GK"]
            role_index = roles.index(def_role) if def_role in roles else 0
            role = st.selectbox("Position / Role", roles, index=role_index)
        with col2:
            fee = st.number_input("Transfer Fee (€ Millions)", min_value=0, max_value=300, value=int(def_fee))
            goals = st.number_input("Goals (Previous Season)", min_value=0, max_value=50, value=int(def_goals))
            assists = st.number_input("Assists (Previous Season)", min_value=0, max_value=40, value=int(def_assists))
        with col3:
            minutes = st.number_input("Minutes Played (Previous Season)", min_value=0, max_value=3800, value=int(def_minutes))
            league_list = list(LEAGUE_DIFFICULTY.keys())
            league_index = league_list.index(def_league) if def_league in league_list else 0
            from_league = st.selectbox("Origin League (Where they play now)", league_list, index=league_index)
            to_league = st.selectbox("Destination League (Where they will move)", league_list)

        submitted = st.form_submit_button("🧠 CALCULATE TRANSFER SCORE", use_container_width=True)

    if submitted:
        result = calculate_transfer_score(age, fee, from_league, to_league, goals, assists, minutes, role)
        score = result["score"]
        pct = f"{score}%"

        st.markdown("---")
        left, right = st.columns([1, 1.5])

        with left:
            # Score Ring (CSS trick)
            ring_color = "#10b981" if score >= 75 else "#f5a623" if score >= 50 else "#ef4444"
            score_html = f"""
<div class="card" style="text-align:center;">
<div style="font-size:0.9rem; color:#9ca3af; margin-bottom:10px; text-transform:uppercase; letter-spacing:1px;">Transfer Success Score</div>
<div style="font-size:6rem; font-weight:900; color:{ring_color}; line-height:1;">{int(score)}</div>
<div style="font-size:1rem; color:{ring_color}; font-weight:700; margin-bottom:15px;">{result['risk']}</div>
<div style="font-size:0.95rem; color:#d1d5db; padding:12px; background:rgba(255,255,255,0.04); border-radius:8px;">{result['recommendation']}</div>
</div>
"""
            st.markdown(score_html, unsafe_allow_html=True)

        with right:
            # Factor Breakdown Radar Chart
            factors = result["factors"]
            categories = list(factors.keys()) + [list(factors.keys())[0]]
            values = list(factors.values()) + [list(factors.values())[0]]
            max_vals = {"Age Factor": 35, "Fee Efficiency": 25, "Adaptation Risk": 20, "Performance History": 20}
            pct_vals = [round((factors[k] / max_vals[k]) * 100) for k in factors.keys()]
            pct_vals_closed = pct_vals + [pct_vals[0]]

            fig = go.Figure()
            fig.add_trace(go.Scatterpolar(
                r=pct_vals_closed,
                theta=categories,
                fill='toself',
                fillcolor='rgba(245, 166, 35, 0.2)',
                line=dict(color='#f5a623', width=2),
                name='Player Profile'
            ))
            fig.update_layout(
                polar=dict(
                    bgcolor='rgba(0,0,0,0)',
                    radialaxis=dict(visible=True, range=[0, 100], gridcolor='rgba(255,255,255,0.08)', tickfont=dict(color='#9ca3af')),
                    angularaxis=dict(gridcolor='rgba(255,255,255,0.08)', tickfont=dict(color='#fff', size=12))
                ),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)

            # Factor breakdown bars
            for factor, val in factors.items():
                max_v = {"Age Factor": 35, "Fee Efficiency": 25, "Adaptation Risk": 20, "Performance History": 20}[factor]
                pct_v = round((val / max_v) * 100)
                bar_html = f"""
<div style="margin-bottom:10px;">
<div style="display:flex; justify-content:space-between; font-size:0.85rem; margin-bottom:4px;">
<span>{factor}</span><span style="color:#f5a623; font-weight:700;">{val}/{max_v} pts</span>
</div>
<div style="background:rgba(255,255,255,0.05); border-radius:4px; height:8px;">
<div style="width:{pct_v}%; background:#f5a623; height:8px; border-radius:4px;"></div>
</div>
</div>
"""
                st.markdown(bar_html, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────
# 📜 HALL OF FAME & SHAME
# ─────────────────────────────────────────────────────────────────
elif nav == "📜 Hall of Fame & Shame":
    st.markdown("<h1>📜 Hall of Fame & Shame</h1>", unsafe_allow_html=True)
    st.markdown("The greatest wins and biggest disasters in modern transfer history — explained by data.")

    tab1, tab2 = st.tabs(["🏆 Hall of Fame — Greatest Transfers", "💸 Hall of Shame — Biggest Flops"])

    with tab1:
        st.markdown("### Top transfers that changed football history:")
        for t in BEST_TRANSFERS:
            card_html = f"""
<div class="card gold-border" style="margin-bottom:16px;">
<div style="display:flex; justify-content:space-between; align-items:flex-start;">
<div>
<div style="font-size:1.8rem; margin-bottom:4px;">{t['icon']}</div>
<h3 style="margin:0;">{t['player']}</h3>
<div style="color:#9ca3af; font-size:0.85rem;">{t['from_club']} → {t['to_club']} ({t['year']}) — <b style="color:#f5a623;">{t['fee']}</b></div>
</div>
<div style="text-align:center; background:rgba(16,185,129,0.1); border-radius:10px; padding:10px 18px; border:1px solid #10b981;">
<div style="font-size:2rem; font-weight:900; color:#10b981;">{t['score']}</div>
<div style="font-size:0.7rem; color:#10b981;">SUCCESS SCORE</div>
</div>
</div>
<p style="margin:12px 0 6px 0; color:#d1d5db;"><b>Outcome:</b> {t['outcome']}</p>
<div style="background:rgba(16,185,129,0.06); border-radius:8px; padding:10px; font-size:0.85rem; color:#9ca3af;"><b style="color:#10b981;">Why it worked:</b> {t['why_great']}</div>
</div>
"""
            st.markdown(card_html, unsafe_allow_html=True)

    with tab2:
        st.markdown("### Biggest transfer regrets in modern football:")
        for t in WORST_TRANSFERS:
            card_html = f"""
<div class="card" style="border:1px solid rgba(239,68,68,0.3); margin-bottom:16px;">
<div style="display:flex; justify-content:space-between; align-items:flex-start;">
<div>
<div style="font-size:1.8rem; margin-bottom:4px;">{t['icon']}</div>
<h3 style="margin:0;">{t['player']}</h3>
<div style="color:#9ca3af; font-size:0.85rem;">{t['from_club']} → {t['to_club']} ({t['year']}) — <b style="color:#ef4444;">{t['fee']}</b></div>
</div>
<div style="text-align:center; background:rgba(239,68,68,0.1); border-radius:10px; padding:10px 18px; border:1px solid #ef4444;">
<div style="font-size:2rem; font-weight:900; color:#ef4444;">{t['score']}</div>
<div style="font-size:0.7rem; color:#ef4444;">SUCCESS SCORE</div>
</div>
</div>
<p style="margin:12px 0 6px 0; color:#d1d5db;"><b>Outcome:</b> {t['outcome']}</p>
<div style="background:rgba(239,68,68,0.06); border-radius:8px; padding:10px; font-size:0.85rem; color:#9ca3af;"><b style="color:#ef4444;">Why it failed:</b> {t['why_failed']}</div>
</div>
"""
            st.markdown(card_html, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────
# 📊 LEAGUE INTELLIGENCE
# ─────────────────────────────────────────────────────────────────
elif nav == "📊 League Intelligence":
    st.markdown("<h1>📊 League Intelligence Report</h1>", unsafe_allow_html=True)
    st.markdown("Which leagues produce the most successful transfers? Which have the biggest failure rates?")

    st.info("💡 **Tip for Fans:** A league with a high 'Success Rate' means that players who moved there generally performed at a high level. A low 'Success Rate' means most expensive transfers failed to deliver.")

    league_stats = get_league_stats(TRANSFERS)
    
    if league_stats:
        df = pd.DataFrame([
            {
                "League": k,
                "Success Rate (%)": v["success_rate"],
                "Successes": v["success"],
                "Partial": v["partial"],
                "Flops": v["flop"],
                "Total": v["total"]
            }
            for k, v in sorted(league_stats.items(), key=lambda x: x[1]["success_rate"], reverse=True)
        ])

        # Bar Chart
        fig = go.Figure()
        colors = ["#10b981" if r >= 50 else "#f5a623" if r >= 30 else "#ef4444" for r in df["Success Rate (%)"]]
        fig.add_trace(go.Bar(
            x=df["League"],
            y=df["Success Rate (%)"],
            marker_color=colors,
            text=[f"{r}%" for r in df["Success Rate (%)"]],
            textposition="outside",
            textfont=dict(color="#fff", size=13, family="Space Grotesk")
        ))
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Space Grotesk", color="#fff"),
            xaxis=dict(gridcolor="rgba(255,255,255,0.05)", tickfont=dict(color="#fff")),
            yaxis=dict(gridcolor="rgba(255,255,255,0.05)", tickfont=dict(color="#9ca3af"), title="Success Rate %"),
            title=dict(text="Transfer Success Rate by Destination League", font=dict(size=16, color="#fff")),
            margin=dict(t=50, b=0),
        )
        st.plotly_chart(fig, use_container_width=True)

        # Data Table
        st.markdown("### Detailed Breakdown")
        st.dataframe(
            df.style.background_gradient(subset=["Success Rate (%)"], cmap="RdYlGn"),
            use_container_width=True,
            hide_index=True
        )

    # League Difficulty Reference
    st.markdown("---")
    st.markdown("<h3>🏟️ League Difficulty Ratings</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:#9ca3af;'>This is how we rate how hard it is to adapt when arriving in each league. Used by our AI model to calculate Adaptation Risk.</p>", unsafe_allow_html=True)

    diff_cols = st.columns(3)
    for i, (league, diff) in enumerate(sorted(LEAGUE_DIFFICULTY.items(), key=lambda x: x[1], reverse=True)):
        with diff_cols[i % 3]:
            color = "#10b981" if diff >= 9 else "#f5a623" if diff >= 7 else "#9ca3af"
            diff_html = f"""
<div class="card" style="text-align:center; padding:14px;">
<div style="font-size:1.5rem; font-weight:900; color:{color};">{diff}/10</div>
<div style="font-size:0.9rem; color:#fff; font-weight:600;">{league}</div>
</div>
"""
            st.markdown(diff_html, unsafe_allow_html=True)
