from db_config import get_connection

class Product:

    def __init__(self, product_id=None, category_id=None, name=None, description=None, price=None, stock=0):
        self.product_id = product_id
        self.category_id = category_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    @staticmethod
    def create_table():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_id INTEGER,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            stock INTEGER DEFAULT 0,
            FOREIGN KEY (category_id) REFERENCES Categories(category_id)
        );
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def insert_product(category_id, name, description, price, stock):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
            INSERT INTO Products (category_id, name, description, price, stock)
            VALUES (?, ?, ?, ?, ?);
            """, (category_id, name, description, price, stock))
            conn.commit()
            print("Product inserted successfully.")
        except Exception as e:
            conn.rollback()
            print("Error inserting product:", e)
        finally:
            conn.close()

    @staticmethod
    def get_all_products():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products;")
        products = cursor.fetchall()
        conn.close()
        return products