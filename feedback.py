```python
import sqlite3

class Feedback:
    def __init__(self):
        self.conn = sqlite3.connect('database.sql')
        self.cursor = self.conn.cursor()

    def handle_feedback(self, feedback_data):
        query_id = feedback_data.get('query_id')
        feedback = feedback_data.get('feedback')

        # Log the feedback in the database
        self.log_feedback(query_id, feedback)

    def log_feedback(self, query_id, feedback):
        self.cursor.execute("""
            INSERT INTO feedback (query_id, feedback) VALUES (?, ?)
        """, (query_id, feedback))

        self.conn.commit()

    def get_feedback(self, query_id):
        self.cursor.execute("""
            SELECT * FROM feedback WHERE query_id = ?
        """, (query_id,))

        return self.cursor.fetchall()
```
