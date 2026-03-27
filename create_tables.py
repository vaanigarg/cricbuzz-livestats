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

cursor.execute("SELECT COUNT(*) FROM players")
count = cursor.fetchone()[0]

if count == 0:
    cursor.execute("""
    INSERT INTO players (name, country, role, batting_style, bowling_style, runs, wickets)
    VALUES
    ('Virat Kohli','India','Batsman','Right-hand bat','Right-arm medium',12898,4),
    ('Joe Root','England','Batsman','Right-hand bat','Right-arm offbreak',11200,28),
    ('Ben Stokes','England','All-rounder','Left-hand bat','Right-arm fast',6200,197)
    """)

conn.commit()
conn.close()

print("Tables created and sample data inserted successfully!")