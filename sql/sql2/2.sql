CREATE INDEX idx_customer_id ON orders (customer_id);

CREATE INDEX idx_composite_id ON order_items(order_id, price);

CREATE INDEX idx_product_name ON order_items(product_name);
