CREATE TABLE customers
(
	id SERIAL PRIMARY KEY,
	name VARCHAR(128) NOT NULL,
	email VARCHAR(128) UNIQUE
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    order_date DATE
);

CREATE TABLE order_items
(
	id SERIAL PRIMARY KEY,
	order_id INT REFERENCES orders(id),
	product_name text,
	quantity INT,
	price NUMERIC
);