from db_config import get_connection

class Customer:

    def __init__(self, customer_id=None, first_name=None, last_name=None, email=None, phone=None, address=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    @staticmethod
    def create_table():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT,
            address TEXT
        );
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def insert_customer(first_name, last_name, email, phone=None, address=None):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
            INSERT INTO Customers (first_name, last_name, email, phone, address)
            VALUES (?, ?, ?, ?, ?);
            """, (first_name, last_name, email, phone, address))
            conn.commit()
            print("Customer inserted successfully.")
        except Exception as e:
            conn.rollback()
            print("Error inserting customer:", e)
        finally:
            conn.close()

    @staticmethod
    def get_all_customers():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Customers;")
        customers = cursor.fetchall()
        conn.close()
        return customers