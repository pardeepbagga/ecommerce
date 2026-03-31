"""
Entrypoint script demonstrating database initialization and CRUD workflows 
for the e-commerce application.
"""
import sys
# Import configuration functions
from db_config import initialize_db, populate_sample_data
# Import model classes from the models package
from models.category import Category
from models.product import Product
from models.customer import Customer
from models.order import Order
from models.order_item import OrderItem
from models.payment import Payment
# Import the consolidated data model for complex operations
from data_model import DataModel

def main():
    """Initialize database, populate sample data, and execute demo operations."""
    
    # SETUP: Create tables and seed sample rows from SQL scripts
    initialize_db()
    populate_sample_data()
    
    # Instantiate DataModel for complex queries and transactions
    dm = DataModel() 
    
    try:
        # ─── CREATE NEW RECORDS ───────────────────────────────────────────
        # Add new category
        Category.insert_category("Gadgets", "Electronics & tech gadgets") 
        new_cat = Category.get_all_categories()[-1]
        print(f"Added category: {new_cat}")

        # Insert a new product linked to the new category
        Product.insert_product(
            category_id=new_cat[0],
            name="Smartwatch",
            description="Fitness tracker + notifications",
            price=199.99,
            stock=150
        )
        new_prod = Product.get_all_products()[-1]
        print(f"Added product: {new_prod}")

        # Insert a new customer
        Customer.insert_customer(
            "Zoe", "Zimmerman", "zoe.z@example.com",
            phone="555-0123", address="101 Demo Lane"
        )
        new_cust = Customer.get_all_customers()[-1]
        print(f"Added customer: {new_cust}")

        # ─── TRANSACTIONAL ORDER CREATION ─────────────────────────────────
        # Define items for the order: (product_id, quantity, unit_price)
        items = [(new_prod[0], 2, new_prod[4])] 

        # Create order and items in a single transaction
        order_id = dm.create_order_with_items(new_cust[0], "101 Demo Lane", items)
        print(f"Created Order ID {order_id} for customer {new_cust[0]}")

        # ─── READ / REPORTS ────────────────────────────────────────────────
        print_reports(dm, new_cust[0])

        # ─── UPDATE OPERATIONS ──────────────────────────────────────────────
        dm.update_product_stock(new_prod[0], new_prod[5] - 2)   # Decrease stock
        dm.update_order_status(order_id, "Completed")          # Mark order as complete
        dm.update_customer_info(new_cust[0], phone="555-0999") # Update contact info

        # ─── DELETE OPERATIONS ──────────────────────────────────────────────
        dm.delete_order_item(order_id, new_prod[0]) # Remove specific item
        dm.delete_payment(order_id)                 # Remove payment records if any
        dm.delete_order(order_id)                   # Remove order header
        dm.delete_customer(new_cust[0])             # Remove customer record
        
        print("\nCleaned up demo order and customer records successfully.")

    except Exception as e:
        print(f"ERROR during demo: {e}", file=sys.stderr)
        
    finally:
        dm.close() # Ensure database connection is always closed

def print_reports(dm, customer_id):
    """
    Print summary reports: best-selling products, order history, 
    unpaid orders, and top customers.
    """
    print("\n--- REPORT: Best-selling products ---")
    for name, sold in dm.get_best_selling_products():
        print(f" • {name}: {sold} sold")

    print("\n--- REPORT: Customer Order History ---")
    for rec in dm.get_customer_order_history(customer_id):
        print(f" Order: {rec}")

    print("\n--- REPORT: Unpaid Orders ---")
    for rec in dm.get_unpaid_orders():
        print(f" Record: {rec}")

    print("\n--- REPORT: Top 5 Customers by Revenue ---")
    for cid, name, total in dm.get_top_customers():
        print(f" • {name} (ID {cid}): ${total:.2f}")

if __name__ == "__main__":
    main()