EXPLAIN ANALYZE SELECT product_name, price
FROM order_items AS oi
WHERE oi.order_id = 123 AND oi.price > 10000;

EXPLAIN ANALYZE SELECT o.id, o.order_date
FROM orders AS o
WHERE o.customer_id = 1;