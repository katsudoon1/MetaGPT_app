"""
database.py
Database class for storing and retrieving game data.
"""

import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("game_data.db")
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()

        # Create game_data table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS game_data (
                id INTEGER PRIMARY KEY,
                balance INTEGER DEFAULT 0,
                win_count INTEGER DEFAULT 0,
                loss_count INTEGER DEFAULT 0
            )
        """)

        self.conn.commit()

    def get_balance(self) -> int:
        cursor = self.conn.cursor()
        cursor.execute("SELECT balance FROM game_data")
        result = cursor.fetchone()
        return result[0] if result else 0

    def update_balance(self, amount: int):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE game_data SET balance = ?", (amount,))
        self.conn.commit()

    def get_win_count(self) -> int:
        cursor = self.conn.cursor()
        cursor.execute("SELECT win_count FROM game_data")
        result = cursor.fetchone()
        return result[0] if result else 0

    def update_win_count(self):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE game_data SET win_count = win_count + 1")
        self.conn.commit()

    def get_loss_count(self) -> int:
        cursor = self.conn.cursor()
        cursor.execute("SELECT loss_count FROM game_data")
        result = cursor.fetchone()
        return result[0] if result else 0

    def update_loss_count(self):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE game_data SET loss_count = loss_count + 1")
        self.conn.commit()
