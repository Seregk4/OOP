EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 1;

-- "Index Scan using idx_customer_id on orders  (cost=0.42..12.46 rows=2 width=12) (actual time=0.028..0.028 rows=0 loops=1)"
-- "  Index Cond: (customer_id = 1)"
-- "Planning Time: 0.067 ms"
-- "Execution Time: 0.043 ms"


EXPLAIN ANALYZE SELECT product_name, price
FROM order_items AS oi
WHERE oi.order_id = 123 AND oi.price > 10000;

-- "Index Scan using idx_composite_id on order_items oi  (cost=0.42..12.46 rows=2 width=23) (actual time=0.023..0.026 rows=3 loops=1)"
-- "  Index Cond: ((order_id = 123) AND (price > '10000'::numeric))"
-- "Planning Time: 0.110 ms"
-- "Execution Time: 0.039 ms"

EXPLAIN ANALYZE SELECT * FROM order_items WHERE product_name = 'товар';

-- "Bitmap Heap Scan on order_items  (cost=5.20..373.59 rows=100 width=35) (actual time=0.020..0.020 rows=0 loops=1)"
-- "  Recheck Cond: (product_name = 'товар'::text)"
-- "  ->  Bitmap Index Scan on idx_product_name  (cost=0.00..5.17 rows=100 width=0) (actual time=0.017..0.017 rows=0 loops=1)"
-- "        Index Cond: (product_name = 'товар'::text)"
-- "Planning Time: 0.058 ms"
-- "Execution Time: 0.033 ms"
