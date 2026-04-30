import sqlite3
import json

DB_NAME = "cache.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cache (
            ticker TEXT PRIMARY KEY,
            data TEXT
        )
    """)

    conn.commit()
    conn.close()


def get_cache(ticker):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT data FROM cache WHERE ticker=?",
        (ticker,)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]

    return None


def save_cache(ticker, data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR REPLACE INTO cache (ticker, data)
        VALUES (?, ?)
        """,
        (ticker, data)
    )

    conn.commit()
    conn.close()