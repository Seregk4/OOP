BEGIN; 
    INSERT INTO orders (order_date) VALUES (NOW()) RETURNING id
    INSERT INTO order_items (order_id, product_name, quantity)
    VALUES (5, 'Apple', 3);

    INSERT INTO order_items (order_id, product_name, quantity)
    VALUES (5, 'Banana', 2);

    INSERT INTO order_items (order_id, product_name, quantity)
    VALUES (5, NULL, 1);
COMMIT;  


BEGIN;

-- пытаемся выполнить блок
SAVEPOINT sp1;

INSERT INTO orders (order_date) VALUES (NOW()) RETURNING id;

-- вставки товаров.
-- если ошибка откат
ROLLBACK TO sp1;

ROLLBACK;
