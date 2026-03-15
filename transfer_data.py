# Transfer Intelligence Engine — Data Layer
# Historical transfers, player stats, and league ratings

# ── League Difficulty Ratings (1-10 scale) ────────────────────────
LEAGUE_DIFFICULTY = {
    "Premier League": 9.5,
    "La Liga": 9.0,
    "Serie A": 8.5,
    "Bundesliga": 8.0,
    "Ligue 1": 7.5,
    "Eredivisie": 6.5,
    "Primeira Liga": 6.0,
    "Saudi Pro League": 5.0,
    "MLS": 4.5,
}

# ── Historical Transfer Dataset ───────────────────────────────────
TRANSFERS = [
    {"player": "Mohamed Salah",        "age": 25, "fee": 42,  "from_league": "Serie A",        "to_league": "Premier League", "role": "Winger",    "goals_prev": 15, "assists_prev": 4,  "minutes_prev": 2800, "result": "Success"},
    {"player": "Virgil van Dijk",      "age": 26, "fee": 75,  "from_league": "Premier League", "to_league": "Premier League", "role": "Defender",  "goals_prev": 2,  "assists_prev": 1,  "minutes_prev": 3000, "result": "Success"},
    {"player": "Alisson Becker",       "age": 25, "fee": 66,  "from_league": "Serie A",        "to_league": "Premier League", "role": "GK",        "goals_prev": 0,  "assists_prev": 0,  "minutes_prev": 3420, "result": "Success"},
    {"player": "Erling Haaland",       "age": 22, "fee": 60,  "from_league": "Bundesliga",     "to_league": "Premier League", "role": "Forward",   "goals_prev": 29, "assists_prev": 8,  "minutes_prev": 1900, "result": "Success"},
    {"player": "Robert Lewandowski",   "age": 33, "fee": 45,  "from_league": "Bundesliga",     "to_league": "La Liga",        "role": "Forward",   "goals_prev": 35, "assists_prev": 8,  "minutes_prev": 3000, "result": "Success"},
    {"player": "Ruben Dias",           "age": 23, "fee": 68,  "from_league": "Primeira Liga",  "to_league": "Premier League", "role": "Defender",  "goals_prev": 3,  "assists_prev": 1,  "minutes_prev": 2700, "result": "Success"},
    {"player": "Kevin De Bruyne",      "age": 23, "fee": 74,  "from_league": "Bundesliga",     "to_league": "Premier League", "role": "Midfielder","goals_prev": 10, "assists_prev": 21, "minutes_prev": 2800, "result": "Success"},
    {"player": "Toni Kroos",           "age": 24, "fee": 25,  "from_league": "Bundesliga",     "to_league": "La Liga",        "role": "Midfielder","goals_prev": 10, "assists_prev": 15, "minutes_prev": 2900, "result": "Success"},
    {"player": "Richarlison",          "age": 25, "fee": 60,  "from_league": "Premier League", "to_league": "Premier League", "role": "Forward",   "goals_prev": 10, "assists_prev": 3,  "minutes_prev": 2300, "result": "Partial"},
    {"player": "João Félix",           "age": 19, "fee": 126, "from_league": "Primeira Liga",  "to_league": "La Liga",        "role": "Forward",   "goals_prev": 15, "assists_prev": 6,  "minutes_prev": 2000, "result": "Partial"},
    {"player": "Antony",               "age": 22, "fee": 95,  "from_league": "Eredivisie",     "to_league": "Premier League", "role": "Winger",    "goals_prev": 12, "assists_prev": 6,  "minutes_prev": 2100, "result": "Flop"},
    {"player": "Hakim Ziyech",         "age": 27, "fee": 40,  "from_league": "Eredivisie",     "to_league": "Premier League", "role": "Winger",    "goals_prev": 16, "assists_prev": 13, "minutes_prev": 2400, "result": "Partial"},
    {"player": "Cody Gakpo",           "age": 23, "fee": 45,  "from_league": "Eredivisie",     "to_league": "Premier League", "role": "Winger",    "goals_prev": 13, "assists_prev": 17, "minutes_prev": 2600, "result": "Partial"},
    {"player": "Ángel Di María",       "age": 26, "fee": 59,  "from_league": "La Liga",        "to_league": "Premier League", "role": "Winger",    "goals_prev": 12, "assists_prev": 18, "minutes_prev": 2700, "result": "Flop"},
    {"player": "Jack Grealish",        "age": 25, "fee": 100, "from_league": "Premier League", "to_league": "Premier League", "role": "Winger",    "goals_prev": 6,  "assists_prev": 10, "minutes_prev": 2500, "result": "Partial"},
    {"player": "Romelu Lukaku (2nd)",  "age": 28, "fee": 113, "from_league": "Serie A",        "to_league": "Premier League", "role": "Forward",   "goals_prev": 24, "assists_prev": 11, "minutes_prev": 2800, "result": "Flop"},
    {"player": "Gareth Bale",          "age": 24, "fee": 91,  "from_league": "Premier League", "to_league": "La Liga",        "role": "Winger",    "goals_prev": 21, "assists_prev": 9,  "minutes_prev": 2900, "result": "Success"},
    {"player": "Neymar Jr.",           "age": 25, "fee": 222, "from_league": "La Liga",        "to_league": "Ligue 1",        "role": "Forward",   "goals_prev": 26, "assists_prev": 14, "minutes_prev": 2800, "result": "Partial"},
    {"player": "Paul Pogba (2nd)",     "age": 23, "fee": 105, "from_league": "Serie A",        "to_league": "Premier League", "role": "Midfielder","goals_prev": 8,  "assists_prev": 12, "minutes_prev": 2900, "result": "Partial"},
    {"player": "Viktor Gyökeres",      "age": 25, "fee": 0,   "from_league": "Premier League", "to_league": "Primeira Liga",  "role": "Forward",   "goals_prev": 8,  "assists_prev": 4,  "minutes_prev": 1800, "result": "Success"},
]

# ── Hall of Fame (Best Transfers) ────────────────────────────────
BEST_TRANSFERS = [
    {
        "player": "Mohamed Salah", "from_club": "AS Roma", "to_club": "Liverpool FC",
        "year": 2017, "fee": "€42M",
        "outcome": "Won the Champions League, Premier League, scored 200+ goals",
        "why_great": "Age 25, peak years. Moved to a stronger league but had elite stats & right profile.",
        "score": 98, "icon": "🏆"
    },
    {
        "player": "Erling Haaland", "from_club": "Borussia Dortmund", "to_club": "Manchester City",
        "year": 2022, "fee": "€60M",
        "outcome": "Scored 36 goals in first PL season — a record. Won the Treble.",
        "why_great": "Age 22 — at the start of his prime. €60M was a bargain for his profile.",
        "score": 97, "icon": "⚡"
    },
    {
        "player": "Virgil van Dijk", "from_club": "Southampton", "to_club": "Liverpool FC",
        "year": 2018, "fee": "€75M",
        "outcome": "Transformed Liverpool's defense. Won PL & UCL in next 2 seasons.",
        "why_great": "Dominant defender at 26. High fee but immediately delivered.",
        "score": 96, "icon": "🛡️"
    },
    {
        "player": "Robert Lewandowski", "from_club": "Bayern Munich", "to_club": "FC Barcelona",
        "year": 2022, "fee": "€45M",
        "outcome": "Scored 58 goals in 2 seasons at Barca, La Liga top scorer.",
        "why_great": "Even at 33, his elite goal-scoring record indicated he'd perform at the highest level.",
        "score": 90, "icon": "🎯"
    },
]

# ── Hall of Shame (Worst Transfers) ──────────────────────────────
WORST_TRANSFERS = [
    {
        "player": "Romelu Lukaku (Return)", "from_club": "Inter Milan", "to_club": "Chelsea FC",
        "year": 2021, "fee": "€113M",
        "outcome": "14 goals in a season. Lost form, relationship with club deteriorated. Sold on loan.",
        "why_failed": "Age 28. Returning to a club he already failed at. Too expensive for his output.",
        "score": 18, "icon": "💸"
    },
    {
        "player": "Antony", "from_club": "Ajax", "to_club": "Manchester United",
        "year": 2022, "fee": "€95M",
        "outcome": "5 goals in 2 seasons. Dropped from the squad.",
        "why_failed": "Moving from Eredivisie (low difficulty) to PL (9.5/10) at massive cost.",
        "score": 12, "icon": "🚨"
    },
    {
        "player": "Ángel Di María", "from_club": "Real Madrid", "to_club": "Manchester United",
        "year": 2014, "fee": "€59M",
        "outcome": "1 season, 4 goals. Family unhappiness contributed to rapid exit.",
        "why_failed": "Great player, wrong club fit. Tactical system mismatch.",
        "score": 20, "icon": "❌"
    },
    {
        "player": "João Félix", "from_club": "Benfica", "to_club": "Atletico Madrid",
        "year": 2019, "fee": "€126M",
        "outcome": "Inconsistent across 4 seasons. Never hit the heights expected.",
        "why_failed": "Too young (19), huge fee pressure, and Atletico's defensive setup didn't suit him.",
        "score": 25, "icon": "⚠️"
    },
]

# ── Player Database for Auto-Fill Predictor ───────────────────────
# Source: TransferMarkt valuations + FBref 2023/24 season data
PLAYER_DATABASE = {
    # ── Forwards / Wingers ──────────────────────────────────────────
    "Erling Haaland (Man City)":          {"club": "Manchester City",   "age": 24, "value": 200, "role": "Forward",    "league": "Premier League", "goals": 27, "assists": 5,  "minutes": 2358},
    "Kylian Mbappé (Real Madrid)":        {"club": "Real Madrid",       "age": 26, "value": 180, "role": "Forward",    "league": "La Liga",        "goals": 33, "assists": 7,  "minutes": 2900},
    "Vinícius Júnior (Real Madrid)":      {"club": "Real Madrid",       "age": 24, "value": 180, "role": "Winger",     "league": "La Liga",        "goals": 23, "assists": 11, "minutes": 2800},
    "Mohamed Salah (Liverpool)":          {"club": "Liverpool FC",      "age": 32, "value": 60,  "role": "Winger",     "league": "Premier League", "goals": 28, "assists": 11, "minutes": 3100},
    "Harry Kane (Bayern Munich)":         {"club": "Bayern Munich",     "age": 31, "value": 100, "role": "Forward",    "league": "Bundesliga",     "goals": 36, "assists": 8,  "minutes": 3100},
    "Robert Lewandowski (Barcelona)":     {"club": "FC Barcelona",      "age": 36, "value": 18,  "role": "Forward",    "league": "La Liga",        "goals": 19, "assists": 5,  "minutes": 2600},
    "Lamine Yamal (Barcelona)":           {"club": "FC Barcelona",      "age": 17, "value": 180, "role": "Winger",     "league": "La Liga",        "goals": 17, "assists": 16, "minutes": 2800},
    "Bukayo Saka (Arsenal)":              {"club": "Arsenal FC",        "age": 23, "value": 170, "role": "Winger",     "league": "Premier League", "goals": 16, "assists": 9,  "minutes": 2700},
    "Raphinha (Barcelona)":               {"club": "FC Barcelona",      "age": 27, "value": 70,  "role": "Winger",     "league": "La Liga",        "goals": 27, "assists": 13, "minutes": 3000},
    "Antoine Griezmann (Atletico)":       {"club": "Atletico Madrid",   "age": 33, "value": 25,  "role": "Forward",    "league": "La Liga",        "goals": 14, "assists": 8,  "minutes": 2500},
    "Julián Álvarez (Atletico Madrid)":   {"club": "Atletico Madrid",   "age": 25, "value": 90,  "role": "Forward",    "league": "La Liga",        "goals": 11, "assists": 9,  "minutes": 2600},
    "Gabriel Martinelli (Arsenal)":       {"club": "Arsenal FC",        "age": 23, "value": 80,  "role": "Winger",     "league": "Premier League", "goals": 8,  "assists": 4,  "minutes": 2100},
    "Ollie Watkins (Aston Villa)":        {"club": "Aston Villa",       "age": 29, "value": 75,  "role": "Forward",    "league": "Premier League", "goals": 19, "assists": 13, "minutes": 3000},
    "Romelu Lukaku (Napoli)":             {"club": "Napoli",            "age": 31, "value": 28,  "role": "Forward",    "league": "Serie A",        "goals": 13, "assists": 3,  "minutes": 2200},
    "Viktor Gyökeres (Sporting)":         {"club": "Sporting CP",       "age": 26, "value": 100, "role": "Forward",    "league": "Primeira Liga",  "goals": 43, "assists": 12, "minutes": 3100},
    "Michael Olise (Bayern Munich)":      {"club": "Bayern Munich",     "age": 23, "value": 65,  "role": "Winger",     "league": "Bundesliga",     "goals": 10, "assists": 6,  "minutes": 1300},
    "Neymar Jr. (Al-Hilal)":              {"club": "Al-Hilal",          "age": 33, "value": 30,  "role": "Winger",     "league": "Saudi Pro League", "goals": 0, "assists": 3,  "minutes": 380},
    "Leroy Sané (Bayern Munich)":         {"club": "Bayern Munich",     "age": 28, "value": 55,  "role": "Winger",     "league": "Bundesliga",     "goals": 12, "assists": 10, "minutes": 2500},

    # ── Midfielders ─────────────────────────────────────────────────
    "Jude Bellingham (Real Madrid)":      {"club": "Real Madrid",       "age": 21, "value": 180, "role": "Midfielder", "league": "La Liga",        "goals": 19, "assists": 11, "minutes": 2900},
    "Kevin De Bruyne (Napoli)":           {"club": "Napoli",            "age": 33, "value": 45,  "role": "Midfielder", "league": "Serie A",        "goals": 3,  "assists": 10, "minutes": 1800},
    "Pedri (Barcelona)":                  {"club": "FC Barcelona",      "age": 22, "value": 110, "role": "Midfielder", "league": "La Liga",        "goals": 6,  "assists": 9,  "minutes": 2100},
    "Rodri (Man City)":                   {"club": "Manchester City",   "age": 28, "value": 100, "role": "Midfielder", "league": "Premier League", "goals": 7,  "assists": 8,  "minutes": 2800},
    "Martin Ødegaard (Arsenal)":          {"club": "Arsenal FC",        "age": 26, "value": 120, "role": "Midfielder", "league": "Premier League", "goals": 8,  "assists": 10, "minutes": 2500},
    "Florian Wirtz (Leverkusen)":         {"club": "Bayer Leverkusen",  "age": 21, "value": 130, "role": "Midfielder", "league": "Bundesliga",     "goals": 18, "assists": 20, "minutes": 2800},
    "Hakan Çalhanoğlu (Inter)":           {"club": "Inter Milan",       "age": 30, "value": 50,  "role": "Midfielder", "league": "Serie A",        "goals": 14, "assists": 10, "minutes": 2800},
    "Cole Palmer (Chelsea)":              {"club": "Chelsea FC",        "age": 22, "value": 160, "role": "Midfielder", "league": "Premier League", "goals": 22, "assists": 11, "minutes": 3000},
    "João Neves (PSG)":                   {"club": "Paris SG",          "age": 20, "value": 60,  "role": "Midfielder", "league": "Ligue 1",        "goals": 3,  "assists": 2,  "minutes": 2700},
    "Bruno Fernandes (Man United)":       {"club": "Manchester United", "age": 30, "value": 60,  "role": "Midfielder", "league": "Premier League", "goals": 10, "assists": 8,  "minutes": 3100},
    "Declan Rice (Arsenal)":              {"club": "Arsenal FC",        "age": 26, "value": 100, "role": "Midfielder", "league": "Premier League", "goals": 7,  "assists": 6,  "minutes": 3000},

    # ── Defenders ───────────────────────────────────────────────────
    "Virgil van Dijk (Liverpool)":        {"club": "Liverpool FC",      "age": 33, "value": 35,  "role": "Defender",   "league": "Premier League", "goals": 4,  "assists": 1,  "minutes": 3000},
    "Ruben Dias (Man City)":              {"club": "Manchester City",   "age": 27, "value": 80,  "role": "Defender",   "league": "Premier League", "goals": 1,  "assists": 2,  "minutes": 2700},
    "Riccardo Calafiori (Arsenal)":       {"club": "Arsenal FC",        "age": 22, "value": 55,  "role": "Defender",   "league": "Premier League", "goals": 2,  "assists": 5,  "minutes": 2600},
    "Trent Alexander-Arnold (Liverpool)": {"club": "Liverpool FC",      "age": 26, "value": 80,  "role": "Defender",   "league": "Premier League", "goals": 3,  "assists": 8,  "minutes": 2700},
    "Josko Gvardiol (Man City)":          {"club": "Manchester City",   "age": 22, "value": 90,  "role": "Defender",   "league": "Premier League", "goals": 6,  "assists": 3,  "minutes": 2500},
    "Jules Koundé (Barcelona)":           {"club": "FC Barcelona",      "age": 26, "value": 70,  "role": "Defender",   "league": "La Liga",        "goals": 2,  "assists": 5,  "minutes": 2600},
    "Alejandro Grimaldo (Leverkusen)":    {"club": "Bayer Leverkusen",  "age": 29, "value": 55,  "role": "Defender",   "league": "Bundesliga",     "goals": 8,  "assists": 13, "minutes": 2900},

    # ── Goalkeepers ─────────────────────────────────────────────────
    "Alisson Becker (Liverpool)":         {"club": "Liverpool FC",      "age": 32, "value": 30,  "role": "GK",         "league": "Premier League", "goals": 0,  "assists": 1,  "minutes": 3420},
    "David Raya (Arsenal)":               {"club": "Arsenal FC",        "age": 29, "value": 50,  "role": "GK",         "league": "Premier League", "goals": 0,  "assists": 0,  "minutes": 3420},
    "Mike Maignan (AC Milan)":            {"club": "AC Milan",          "age": 29, "value": 55,  "role": "GK",         "league": "Serie A",        "goals": 0,  "assists": 0,  "minutes": 3240},
    "Gregor Kobel (Dortmund)":            {"club": "Borussia Dortmund", "age": 27, "value": 55,  "role": "GK",         "league": "Bundesliga",     "goals": 0,  "assists": 0,  "minutes": 3060},
    "Jan Oblak (Atletico)":               {"club": "Atletico Madrid",   "age": 31, "value": 35,  "role": "GK",         "league": "La Liga",        "goals": 0,  "assists": 0,  "minutes": 3420},
}
