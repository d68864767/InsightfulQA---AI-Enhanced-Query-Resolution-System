```sql
BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS queries (
    id INTEGER PRIMARY KEY,
    query TEXT NOT NULL,
    language TEXT NOT NULL,
    response TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY,
    query_id INTEGER NOT NULL,
    feedback TEXT NOT NULL,
    FOREIGN KEY(query_id) REFERENCES queries(id)
);

COMMIT;
```
