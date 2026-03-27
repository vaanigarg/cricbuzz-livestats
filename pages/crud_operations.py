import streamlit as st
from utils.db_connection import get_connection
import pandas as pd

conn = get_connection()
cursor = conn.cursor()

st.title("CRUD Operations")

st.subheader("Add Player")

name = st.text_input("Name")
country = st.text_input("Country")

if st.button("Add"):
    cursor.execute("INSERT INTO players (name, country) VALUES (?, ?)", (name, country))
    conn.commit()
    st.success("Added!")

st.subheader("All Players")

df = pd.read_sql_query("SELECT * FROM players", conn)
st.dataframe(df)

st.subheader("Delete Player")

player_id = st.number_input("Enter Player ID", min_value=1)

if st.button("Delete"):
    cursor.execute("DELETE FROM players WHERE id=?", (player_id,))
    conn.commit()
    st.success("Deleted!")