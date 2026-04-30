import sqlite3

DB_PATH = "cache.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS cache (
            ticker TEXT PRIMARY KEY,
            summary TEXT
        )
    """)
    conn.commit()
    conn.close()


def get_cache(ticker):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT summary FROM cache WHERE ticker = ?", (ticker,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None


def save_cache(ticker, summary):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT OR REPLACE INTO cache (ticker, summary) VALUES (?, ?)",
        (ticker, summary),
    )
    conn.commit()
    conn.close()