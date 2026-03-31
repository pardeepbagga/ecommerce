-- Products table stores all product details and links to Categories

CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    stock INTEGER DEFAULT 0,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

INSERT INTO Products (category_id, name, description, price, stock) VALUES
(1, 'Smartphone', 'Latest model smartphone', 699.99, 50),
(1, 'Laptop', 'High-performance laptop', 999.99, 30),
(1, 'Headphones', 'Noise-cancelling headphones', 199.99, 75),
(2, 'Novel', 'Best-selling novel', 14.99, 100),
(2, 'Science Book', 'Educational science book', 29.99, 60),
(3, 'T-Shirt', 'Cotton T-shirt', 9.99, 200),
(3, 'Jeans', 'Denim jeans', 49.99, 100),
(4, 'Sofa', 'Comfortable 3-seater sofa', 499.99, 10),
(4, 'Coffee Maker', 'Automatic coffee maker', 79.99, 25),
(5, 'Action Figure', 'Popular superhero action figure', 19.99, 150);