from db_config import get_connection

class Payment:

    @staticmethod
    def make_payment(order_id, payment_method, amount):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
            INSERT INTO Payments (order_id, payment_method, amount)
            VALUES (?, ?, ?);
            """, (order_id, payment_method, amount))
            conn.commit()
            print("Payment recorded successfully.")
        except Exception as e:
            conn.rollback()
            print("Error processing payment:", e)
        finally:
            conn.close()

    @staticmethod
    def get_all_payments():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Payments;")
        payments = cursor.fetchall()
        conn.close()
        return payments