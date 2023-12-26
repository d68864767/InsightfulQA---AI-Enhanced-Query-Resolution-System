```python
import sqlite3

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect('database.sql')
        self.cursor = self.conn.cursor()

        # Create tables if they don't exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS queries (
                id INTEGER PRIMARY KEY,
                query TEXT NOT NULL,
                language TEXT NOT NULL,
                response TEXT NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY,
                query_id INTEGER NOT NULL,
                feedback TEXT NOT NULL,
                FOREIGN KEY(query_id) REFERENCES queries(id)
            )
        """)

    def log_query(self, query, language, response):
        self.cursor.execute("""
            INSERT INTO queries (query, language, response) VALUES (?, ?, ?)
        """, (query, language, response))

        self.conn.commit()

    def log_feedback(self, query_id, feedback):
        self.cursor.execute("""
            INSERT INTO feedback (query_id, feedback) VALUES (?, ?)
        """, (query_id, feedback))

        self.conn.commit()

    def get_query(self, query_id):
        self.cursor.execute("""
            SELECT * FROM queries WHERE id = ?
        """, (query_id,))

        return self.cursor.fetchone()

    def get_feedback(self, query_id):
        self.cursor.execute("""
            SELECT * FROM feedback WHERE query_id = ?
        """, (query_id,))

        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
```
