CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date TEXT DEFAULT (datetime('now')),
    shipping_address TEXT NOT NULL,
    status TEXT DEFAULT 'Pending',
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);