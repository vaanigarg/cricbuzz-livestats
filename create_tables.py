from utils.db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    country TEXT,
    role TEXT,
    batting_style TEXT,
    bowling_style TEXT,
    runs INTEGER,
    wickets INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS matches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    team1 TEXT,
    team2 TEXT,
    winner TEXT,
    venue TEXT,
    date TEXT
)
""")

conn.commit()
conn.close()

print("Tables created successfully!")