# db_config.py
import sqlite3
import os

DB_PATH = os.path.join(os.getcwd(), "ecommerce.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    # Enforce foreign key constraints
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()
    # Execute the SQL scripts
    with open("sql/categories.sql", "r") as file:
        cursor.executescript(file.read())
    with open("sql/products.sql", "r") as file:
        cursor.executescript(file.read())
    with open("sql/customers.sql", "r") as file:
        cursor.executescript(file.read())
    with open("sql/orders.sql", "r") as file:
        cursor.executescript(file.read())
    with open("sql/order_items.sql", "r") as file:
        cursor.executescript(file.read())
    with open("sql/payments.sql", "r") as file:
        cursor.executescript(file.read())
    
    conn.commit()
    conn.close()

def populate_sample_data():
    """Separated function to seed the database."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        with open("sql/populate_sample_data.sql", "r") as file:
            cursor.executescript(file.read())
        conn.commit()
        print("Sample data populated successfully.")
    except Exception as e:
        print(f"Error populating data: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    initialize_db()
    print("Database initialized successfully.")