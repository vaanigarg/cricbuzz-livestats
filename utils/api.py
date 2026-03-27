import requests
import streamlit as st

API_KEY = st.secrets["53a1474161mshd6033a30a7fc5efp1bb199jsn59bfb3a9447f"]
API_HOST = "cricbuzz-cricket.p.rapidapi.com"

def get_live_matches():
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print("Error:", response.status_code)
            return None

    except Exception as e:
        print("API Error:", e)
        return None