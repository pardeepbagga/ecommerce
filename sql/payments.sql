CREATE TABLE IF NOT EXISTS Payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    payment_method TEXT NOT NULL,
    amount REAL NOT NULL,
    payment_date TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);

-- TODO: Add INSERT statements here if needed