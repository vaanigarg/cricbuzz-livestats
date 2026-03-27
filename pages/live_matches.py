import streamlit as st
from utils.api import get_live_matches
from utils.db_connection import get_connection

st.title("Live Matches")

conn = get_connection()
cursor = conn.cursor()

data = get_live_matches()

if data:
    
    st.json(data)

    if "data_inserted" not in st.session_state:
        try:
            cursor.execute("""
            INSERT INTO matches (team1, team2, winner, venue, date)
            VALUES (?, ?, ?, ?, date('now'))
            """, ("India", "Australia", "India", "Mumbai"))

            conn.commit()
            st.session_state["data_inserted"] = True

        except Exception:
            pass

else:
    st.error("Failed to fetch live data")