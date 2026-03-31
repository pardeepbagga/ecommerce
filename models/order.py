from db_config import get_connection

class Order:

    @staticmethod
    def create_order(customer_id, shipping_address, status="Pending"):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
            INSERT INTO Orders (customer_id, shipping_address, status)
            VALUES (?, ?, ?);
            """, (customer_id, shipping_address, status))
            conn.commit()
            print("Order created successfully.")
            return cursor.lastrowid
        except Exception as e:
            conn.rollback()
            print("Error creating order:", e)
        finally:
            conn.close()

    @staticmethod
    def get_all_orders():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Orders;")
        orders = cursor.fetchall()
        conn.close()
        return orders