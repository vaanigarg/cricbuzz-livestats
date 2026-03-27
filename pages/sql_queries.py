import streamlit as st
import pandas as pd
from utils.db_connection import get_connection

st.title("SQL Analytics - 25 Queries")

conn = get_connection()

option = st.selectbox("Choose Query", [

    "Q1: Players from India",
    "Q2: Matches in last 30 days",
    "Q3: Top run scorers",
    "Q4: All players (venue not available)",
    "Q5: Matches won by each team",
    "Q6: Player role count",
    "Q7: Highest score",
    "Q8: Matches in 2024",

    "Q9: All-rounders with >1000 runs & >50 wickets",
    "Q10: Last 20 matches",
    "Q11: Player performance (basic)",
    "Q12: Matches per team",
    "Q13: Partnerships (not available)",
    "Q14: Top bowlers",
    "Q15: All matches (close match simplified)",
    "Q16: Player yearly performance (not available)",

    "Q17: Toss analysis (not available)",
    "Q18: Economical bowlers",
    "Q19: Consistent batsmen",
    "Q20: Player list",
    "Q21: Player ranking system",
    "Q22: Head-to-head matches",
    "Q23: Recent form (not available)",
    "Q24: Best partnerships (not available)",
    "Q25: Performance over time (not available)"
])

query = ""

if option == "Q1: Players from India":
    query = "SELECT name, role, batting_style, bowling_style FROM players WHERE country='India'"

elif option == "Q2: Matches in last 30 days":
    query = "SELECT * FROM matches WHERE date >= DATE('now','-30 days') ORDER BY date DESC"

elif option == "Q3: Top run scorers":
    query = "SELECT name, runs FROM players ORDER BY runs DESC LIMIT 10"

elif option == "Q4: All players (venue not available)":
    query = "SELECT * FROM players"

elif option == "Q5: Matches won by each team":
    query = "SELECT winner, COUNT(*) as wins FROM matches GROUP BY winner ORDER BY wins DESC"

elif option == "Q6: Player role count":
    query = "SELECT role, COUNT(*) as count FROM players GROUP BY role"

elif option == "Q7: Highest score":
    query = "SELECT MAX(runs) as highest_score FROM players"

elif option == "Q8: Matches in 2024":
    query = "SELECT * FROM matches WHERE date LIKE '2024%'"

elif option == "Q9: All-rounders with >1000 runs & >50 wickets":
    query = "SELECT name, runs, wickets FROM players WHERE role='All-rounder' AND runs>1000 AND wickets>50"

elif option == "Q10: Last 20 matches":
    query = "SELECT * FROM matches ORDER BY date DESC LIMIT 20"

elif option == "Q11: Player performance (basic)":
    query = "SELECT name, runs, wickets FROM players"

elif option == "Q12: Matches per team":
    query = "SELECT team1, COUNT(*) as matches_played FROM matches GROUP BY team1"

elif option == "Q13: Partnerships (not available)":
    query = "SELECT 'Not Available in Current Dataset' as Message"

elif option == "Q14: Top bowlers":
    query = "SELECT name, wickets FROM players ORDER BY wickets DESC"

elif option == "Q15: All matches (close match simplified)":
    query = "SELECT * FROM matches"

elif option == "Q16: Player yearly performance (not available)":
    query = "SELECT 'Not Available in Current Dataset' as Message"

elif option == "Q17: Toss analysis (not available)":
    query = "SELECT 'Not Available in Current Dataset' as Message"

elif option == "Q18: Economical bowlers":
    query = "SELECT name, wickets FROM players WHERE wickets > 10 ORDER BY wickets DESC"

elif option == "Q19: Consistent batsmen":
    query = "SELECT name, runs FROM players ORDER BY runs DESC"

elif option == "Q20: Player list":
    query = "SELECT name FROM players"

elif option == "Q21: Player ranking system":
    query = "SELECT name, (runs*0.01 + wickets*2) as score FROM players ORDER BY score DESC"

elif option == "Q22: Head-to-head matches":
    query = "SELECT team1, team2, COUNT(*) as matches FROM matches GROUP BY team1, team2"

elif option == "Q23: Recent form (not available)":
    query = "SELECT 'Not Available in Current Dataset' as Message"

elif option == "Q24: Best partnerships (not available)":
    query = "SELECT 'Not Available in Current Dataset' as Message"

elif option == "Q25: Performance over time (not available)":
    query = "SELECT 'Not Available in Current Dataset' as Message"

if st.button("Run Query"):
    try:
        df = pd.read_sql_query(query, conn)
        st.dataframe(df)
    except Exception as e:
        st.error(str(e))