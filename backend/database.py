"""
Database connection and setup for iStateSell
"""

import sqlite3
from contextlib import contextmanager

class DatabaseManager:
    def __init__(self, db_path='istatesell.db'):
        self.db_path = db_path
    
    @contextmanager
    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()
    
    def initialize_database(self):
        """Create initial database tables"""
        with self.get_connection() as conn:
            with open('database/schema.sql', 'r') as f:
                conn.executescript(f.read())
            print("✅ Database initialized successfully!")

# Singleton instance
db = DatabaseManager()
