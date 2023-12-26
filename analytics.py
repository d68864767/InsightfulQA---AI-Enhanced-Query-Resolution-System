```python
import sqlite3
from collections import Counter

class Analytics:
    def __init__(self):
        self.conn = sqlite3.connect('database.sql')
        self.cursor = self.conn.cursor()

    def log_query(self, query, language):
        self.cursor.execute("""
            INSERT INTO queries (query, language) VALUES (?, ?)
        """, (query, language))

        self.conn.commit()

    def get_analytics(self):
        # Get all queries
        self.cursor.execute("""
            SELECT query, language FROM queries
        """)
        all_queries = self.cursor.fetchall()

        # Get all feedback
        self.cursor.execute("""
            SELECT feedback FROM feedback
        """)
        all_feedback = self.cursor.fetchall()

        # Count the number of queries per language
        language_counts = Counter([query[1] for query in all_queries])

        # Count the number of positive and negative feedback
        feedback_counts = Counter([feedback[0] for feedback in all_feedback])

        # Prepare the analytics data
        analytics_data = {
            'total_queries': len(all_queries),
            'queries_per_language': dict(language_counts),
            'total_feedback': len(all_feedback),
            'feedback_counts': dict(feedback_counts),
        }

        return analytics_data

    def close(self):
        self.conn.close()
```
