from utils.db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

players = [
    ("Virat Kohli", "India", "Batsman", "Right-hand", "None", 13000, 5),
    ("Rohit Sharma", "India", "Batsman", "Right-hand", "Off-spin", 11000, 10),
    ("Ben Stokes", "England", "All-rounder", "Left-hand", "Fast", 6000, 200),
    ("Joe Root", "England", "Batsman", "Right-hand", "Off-spin", 10000, 50),
    ("David Warner", "Australia", "Batsman", "Left-hand", "None", 9000, 2)
]

cursor.executemany("""
INSERT INTO players (name, country, role, batting_style, bowling_style, runs, wickets)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", players)

matches = [
    ("India", "Australia", "India", "Mumbai", "2024-01-10"),
    ("England", "India", "England", "London", "2024-02-15"),
    ("Australia", "England", "Australia", "Sydney", "2024-03-20")
]

cursor.executemany("""
INSERT INTO matches (team1, team2, winner, venue, date)
VALUES (?, ?, ?, ?, ?)
""", matches)

conn.commit()
conn.close()

print("Sample data inserted!")