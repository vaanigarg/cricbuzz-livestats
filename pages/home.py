import streamlit as st

st.title("Cricbuzz LiveStats")

st.markdown("### Real-Time Cricket Analytics Dashboard")

st.write("""
This platform provides:
- Live Match Updates
- Player Statistics
- SQL-Based Analytics
- CRUD Operations
""")

st.markdown("### Key Statistics")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Players", 5)

with col2:
    st.metric("Total Matches", 3)

st.info("Use the sidebar to navigate between pages")