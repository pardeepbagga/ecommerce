# models/category.py
from db_config import get_connection

class Category: # Rename from Customer
    @staticmethod
    def create_table():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Categories (
                category_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT
            );
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def insert_category(name, description=None): # Rename from insert_customer
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Categories (name, description) VALUES (?, ?);",
                (name, description)
            )
            conn.commit()
            print("Category inserted successfully.")
        except Exception as e:
            conn.rollback()
            print("Error inserting category:", e)
        finally:
            conn.close()

    @staticmethod
    def get_all_categories(): # Rename from get_all_customers
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Categories;")
        categories = cursor.fetchall()
        conn.close()
        return categories