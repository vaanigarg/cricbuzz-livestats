import streamlit as st

st.set_page_config(page_title="Cricbuzz LiveStats", layout="wide")

st.title("Cricbuzz LiveStats Dashboard")

st.markdown("Welcome to Real-Time Cricket Analytics Platform")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Home", "Live Matches", "Top Stats", "SQL Queries", "CRUD Operations"]
)

if page == "Home":
    import pages.home

elif page == "Live Matches":
    import pages.live_matches

elif page == "Top Stats":
    import pages.top_stats

elif page == "SQL Queries":
    import pages.sql_queries

elif page == "CRUD Operations":
    import pages.crud_operations