import sqlite3
from db_config import get_connection

class DataModel:
    """Class to encapsulate database CRUD, reporting, and transactional operations."""
    
    def __init__(self):
        """Establish a SQLite connection with foreign keys enabled."""
        self.conn = get_connection()

    def close(self):
        """Close the active database connection."""
        self.conn.close()

    def get_best_selling_products(self):
        """Return list of tuples (product_name, total_sold), sorted descending."""
        cursor = self.conn.cursor()
        query = (
            "SELECT P.name, SUM(OI.quantity) AS total_sold "
            "FROM OrderItems OI "
            "JOIN Products P ON OI.product_id = P.product_id "
            "GROUP BY P.name ORDER BY total_sold DESC;"
        )
        cursor.execute(query)
        return cursor.fetchall()

    def get_customer_order_history(self, customer_id):
        """Fetch order history for a given customer_id including order total."""
        cursor = self.conn.cursor()
        query = (
            "SELECT O.order_id, O.order_date, O.status, "
            "SUM(OI.quantity * OI.unit_price) AS order_total "
            "FROM Orders O JOIN OrderItems OI ON O.order_id = OI.order_id "
            "WHERE O.customer_id = ? "
            "GROUP BY O.order_id;"
        )
        cursor.execute(query, (customer_id,))
        return cursor.fetchall()

    def update_product_stock(self, product_id, new_stock):
        """Update stock for a product; return number of rows affected."""
        cursor = self.conn.cursor()
        cursor.execute("UPDATE Products SET stock = ? WHERE product_id = ?;", (new_stock, product_id))
        self.conn.commit()
        return cursor.rowcount

    def delete_order_item(self, order_id, product_id):
        """Delete a specific item from an order; return number of rows affected."""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM OrderItems WHERE order_id = ? AND product_id = ?;", (order_id, product_id))
        self.conn.commit()
        return cursor.rowcount

    def create_order_with_items(self, customer_id, shipping_address, items):
        """Insert an order and its items in a single transaction."""
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Orders (customer_id, shipping_address) VALUES (?, ?);",
                (customer_id, shipping_address)
            )
            order_id = cursor.lastrowid
            
            for product_id, quantity, unit_price in items:
                cursor.execute(
                    "INSERT INTO OrderItems (order_id, product_id, quantity, unit_price) VALUES (?, ?, ?, ?);",
                    (order_id, product_id, quantity, unit_price)
                )
            self.conn.commit()
            return order_id
        except Exception as e:
            self.conn.rollback()
            print(f"Transaction failed: {e}")
            return None

    def get_unpaid_orders(self):
        """Fetch orders that do not have a corresponding entry in the Payments table."""
        cursor = self.conn.cursor()
        query = "SELECT * FROM Orders WHERE order_id NOT IN (SELECT order_id FROM Payments);"
        cursor.execute(query)
        return cursor.fetchall()

    def get_top_customers(self):
        """Fetch the top 5 customers based on total spending."""
        cursor = self.conn.cursor()
        query = """
            SELECT C.customer_id, C.first_name || ' ' || C.last_name AS name, SUM(P.amount) as total 
            FROM Customers C 
            JOIN Orders O ON C.customer_id = O.customer_id 
            JOIN Payments P ON O.order_id = P.order_id 
            GROUP BY C.customer_id 
            ORDER BY total DESC 
            LIMIT 5;
        """
        cursor.execute(query)
        return cursor.fetchall()

    def update_order_status(self, order_id, status):
        """Update the status of an existing order."""
        cursor = self.conn.cursor()
        cursor.execute("UPDATE Orders SET status = ? WHERE order_id = ?;", (status, order_id))
        self.conn.commit()

    def update_customer_info(self, customer_id, phone):
        """Update a customer's phone number."""
        cursor = self.conn.cursor()
        cursor.execute("UPDATE Customers SET phone = ? WHERE customer_id = ?;", (phone, customer_id))
        self.conn.commit()

    def delete_payment(self, order_id):
        """Delete payment records for a specific order."""
        self.conn.execute("DELETE FROM Payments WHERE order_id = ?;", (order_id,))
        self.conn.commit()

    def delete_order(self, order_id):
        """Delete an order record."""
        self.conn.execute("DELETE FROM Orders WHERE order_id = ?;", (order_id,))
        self.conn.commit()

    def delete_customer(self, customer_id):
        """Delete a customer record."""
        self.conn.execute("DELETE FROM Customers WHERE customer_id = ?;", (customer_id,))
        self.conn.commit()