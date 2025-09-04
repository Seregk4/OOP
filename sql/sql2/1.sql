INSERT INTO customers (name, email)
SELECT
    'Клиент ' || generate_series(1, 1000000),
    'test' || generate_series(1, 1000000) || '@123aa.com';


INSERT INTO orders (customer_id, order_date)
SELECT
    (RANDOM() * 1000000 + 1)::INT,
    CURRENT_DATE - (RANDOM() * 365)::INT
FROM
    generate_series(1, 1000000);


INSERT INTO order_items (order_id, product_name, quantity, price)
SELECT
    (RANDOM() * (SELECT MAX(id) FROM orders) + 1)::INT,
    'Товар ' || (RANDOM() * 10000)::INT,
    (RANDOM() * 100)::INT + 1,
    (RANDOM() * 100000)::NUMERIC(10, 2)
FROM
    generate_series(1, 1000000);