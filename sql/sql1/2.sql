-- ALTER SEQUENCE orders_id_seq RESTART WITH 1;

INSERT INTO customers (name, email)
VALUES
('Вася Пупкин', 'uniq1@gmail.com'),
('Иван Питонов', 'uniq113@gmail.com'),
('Колыыыма', 'uniq1231@gmail.com');


INSERT INTO orders (customer_id, order_date)
VALUES
(1, '2025-09-01'),  
(2, '2025-09-02'),  
(1, '2025-09-02');  

INSERT INTO order_items (order_id, product_name, quantity, price)
VALUES
(1, 'тестовый товар1', 10, 1000),
(2, 'тестовый товар2', 0, 1013400.5),
(1, 'тестовый товар3', 100, 10),
(2, 'тестовый товар4', 11, 100),
(2, 'тестовый товар5', 11, 1000123);
