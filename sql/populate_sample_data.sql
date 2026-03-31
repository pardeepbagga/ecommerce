PRAGMA foreign_keys = OFF;

DELETE FROM sqlite_sequence WHERE name = 'Categories';
DELETE FROM sqlite_sequence WHERE name = 'Products';
DELETE FROM sqlite_sequence WHERE name = 'Customers';
DELETE FROM sqlite_sequence WHERE name = 'Orders';
DELETE FROM sqlite_sequence WHERE name = 'OrderItems';
DELETE FROM sqlite_sequence WHERE name = 'Payments';

PRAGMA foreign_keys = ON;

-- Categories
INSERT OR IGNORE INTO Categories (name, description) VALUES
('Electronics','Devices and gadgets'),
('Books','Fiction and non-fiction literature'),
('Clothing','Men and women apparel'),
('Home','Home appliances and furniture'),
('Toys','Toys and games for children');

-- Products
INSERT OR IGNORE INTO Products (category_id, name, description, price, stock) VALUES
(1,'Smartphone','Latest model smartphone',699.99,50),
(1,'Laptop','High performance laptop',999.99,30),
(1,'Headphones','Noise-cancelling headphones',199.99,75),
(2,'Novel','Best-selling novel',14.99,100),
(2,'Science Book','Educational science book',29.99,60),
(3,'T-Shirt','Cotton T-shirt',9.99,200),
(3,'Jeans','Denim jeans',49.99,100),
(4,'Sofa','Comfortable 3-seater sofa',499.99,10),
(4,'Coffee Maker','Automatic coffee maker',79.99,25),
(5,'Action Figure','Popular superhero action figure',19.99,150);

-- Customers
INSERT OR IGNORE INTO Customers (first_name,last_name,email,phone,address) VALUES
('John','Doe','john.doe@example.com','555-0101','123 Elm St'),
('Jane','Smith','jane.smith@example.com','555-0102','456 Oak St'),
('Alice','Johnson','alice.johnson@example.com','555-0103','789 Pine St'),
('Bob','Williams','bob.williams@example.com','555-0104','321 Maple St'),
('Charlie','Brown','charlie.brown@example.com','555-0105','654 Cedar St'),
('Diana','Prince','diana.prince@example.com','555-0106','987 Birch St'),
('Ethan','Hunt','ethan.hunt@example.com','555-0107','159 Walnut St'),
('Fiona','Gallagher','fiona.gallagher@example.com','555-0108','753 Spruce St'),
('George','Martin','george.martin@example.com','555-0109','852 Ash St'),
('Hannah','Lee','hannah.lee@example.com','555-0110','147 Palm St');

-- Orders
INSERT OR IGNORE INTO Orders (customer_id, shipping_address, status) VALUES
(1,'123 Elm St','Pending'),
(2,'456 Oak St','Shipped'),
(3,'789 Pine St','Delivered'),
(4,'321 Maple St','Cancelled'),
(5,'654 Cedar St','Pending'),
(6,'987 Birch St','Shipped'),
(7,'159 Walnut St','Delivered'),
(8,'753 Spruce St','Pending'),
(9,'852 Ash St','Delivered'),
(10,'147 Palm St','Shipped');

-- OrderItems
INSERT OR IGNORE INTO OrderItems (order_id, product_id, quantity, unit_price) VALUES
(1,1,2,699.99),
(1,3,1,199.99),
(2,2,1,999.99),
(2,4,3,14.99),
(3,5,2,29.99),
(4,6,5,9.99),
(5,7,1,49.99),
(6,8,1,499.99),
(7,9,2,79.99),
(8,10,4,19.99),
(9,1,1,699.99),
(10,2,2,999.99),
(10,4,1,14.99),
(3,6,3,9.99);

-- Payments
INSERT OR IGNORE INTO Payments (order_id, payment_method, amount) VALUES
(1,'Credit Card',1599.97),
(2,'PayPal',1044.96),
(3,'Debit Card',89.95),
(4,'Credit Card',49.95),
(5,'Credit Card',149.97),
(6,'PayPal',499.99),
(7,'Debit Card',159.98),
(8,'Credit Card',79.96),
(9,'Debit Card',699.99),
(10,'Credit Card',2014.97);