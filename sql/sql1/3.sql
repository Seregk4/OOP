-- SELECT o.id, o.order_date 
-- FROM customers AS c
-- JOIN orders AS o ON c.id = o.customer_id
-- WHERE c.name = 'Вася Пупкин'

-- SELECT product_name, quantity, price
-- FROM orders AS o
-- JOIN order_items AS oi ON o.id = oi.order_id
-- WHERE o.id = 1
-- ORDER BY price DESC

SELECT SUM(price * quantity) AS total_spent
FROM customers AS c
JOIN orders AS o ON c.id = o.customer_id
JOIN order_items AS oi ON o.id = oi.order_id
GROUP BY name
HAVING SUM(price * quantity) > 5000
