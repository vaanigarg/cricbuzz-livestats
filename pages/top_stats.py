import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.db_connection import get_connection

st.title("Top Player Stats")

conn = get_connection()

df = pd.read_sql_query("SELECT name, runs FROM players", conn)

st.dataframe(df)

fig, ax = plt.subplots()
ax.bar(df["name"], df["runs"])

plt.xticks(rotation=45)

st.pyplot(fig)