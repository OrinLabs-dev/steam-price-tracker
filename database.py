#database.py
import sqlite3
import logging
import os
import sys
LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'debug.log')

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s'
)
ERROR_LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'error_log.txt')

def create_table():
    conn = sqlite3.connect('prices.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS price_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                game_name TEXT,
                url TEXT,
                price REAL,
                timestamp TEXT
                )
    """)

    conn.commit()

def insert_price(game_name, url, price, timestamp):
    conn = sqlite3.connect('prices.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO price_history (game_name, url, price, timestamp)
        VALUES (?, ?, ?, ?)
""", (game_name, url, price, timestamp))
    conn.commit()

def get_all_prices():
    conn = sqlite3.connect('prices.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM price_history")
    rows = cursor.fetchall()
    conn.commit()
    return rows

def get_last_price(url):
    conn = sqlite3.connect('prices.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT price FROM price_history
        WHERE url = ?
        ORDER BY id DESC
        LIMIT 1
""", (url,))
    row = cursor.fetchone()
    if row is None:
        return None
    return row[0]



if __name__ == "__main__":
    from datetime import datetime
    now = datetime.now().strftime("%y-%b-%d")
    create_table()
    insert_price('Red Dead Redemption 2', 'https://store.steampowered.com/app/1174180/Red_Dead_Redemption_2/', 14.99, now)
    print(get_all_prices())
    print(get_last_price('https://store.steampowered.com/app/1174180/Red_Dead_Redemption_2/'))