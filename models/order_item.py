from db_config import get_connection

class OrderItem:

    @staticmethod
    def add_item(order_id, product_id, quantity, unit_price):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
            INSERT INTO OrderItems (order_id, product_id, quantity, unit_price)
            VALUES (?, ?, ?, ?);
            """, (order_id, product_id, quantity, unit_price))
            conn.commit()
            print("Order item added.")
        except Exception as e:
            conn.rollback()
            print("Error adding order item:", e)
        finally:
            conn.close()