CREATE TABLE IF NOT EXISTS Categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);