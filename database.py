import sqlite3


def get_connection():
    conn = sqlite3.connect("karna.db", check_same_thread=False)
    return conn


# ---------------- INIT DATABASE ----------------
def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rounds INTEGER,
            score INTEGER,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


# ---------------- ADD SCORE ----------------
def add_score(rounds, score):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO scores (rounds, score) VALUES (?, ?)",
        (rounds, score)
    )

    conn.commit()
    conn.close()


# ---------------- GET SCORES ----------------
def get_scores():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM scores ORDER BY date DESC"
    )

    data = cursor.fetchall()

    conn.close()
    return data


# ---------------- DAILY RECORDS ----------------
def add_record(date, arrows, practice_time, mistakes, learnings):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS daily_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            arrows INTEGER,
            practice_time REAL,
            mistakes TEXT,
            learnings TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO daily_records
        (date, arrows, practice_time, mistakes, learnings)
        VALUES (?, ?, ?, ?, ?)
    """, (date, arrows, practice_time, mistakes, learnings))

    conn.commit()
    conn.close()


def get_records():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS daily_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            arrows INTEGER,
            practice_time REAL,
            mistakes TEXT,
            learnings TEXT
        )
    """)

    cursor.execute(
        "SELECT * FROM daily_records ORDER BY date DESC"
    )

    data = cursor.fetchall()

    conn.close()
    return data