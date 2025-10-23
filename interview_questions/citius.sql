INSERT INTO customers (customer_id, name, email, signup_date) VALUES
(1, 'Alice Johnson', 'alice@example.com', '2023-01-15'),
(2, 'Bob Smith', 'bob@example.com', '2023-02-10'),
(3, 'Charlie Rose', 'charlie@example.com', '2023-03-05'),
(4, 'Diana Prince', 'diana@example.com', '2023-04-20'),
(5, 'Ethan Hunt', 'ethan@example.com', '2023-05-01');

INSERT INTO orders (order_id, customer_id, order_date, amount) VALUES
(101, 1, '2023-01-20', 150.00),
(102, 1, '2023-02-15', 200.00),
(103, 2, '2023-02-18', 350.00),
(104, 3, '2023-03-15', 120.00),
(105, 3, '2023-04-01', 180.00),
(106, 5, '2023-05-15', 220.00);

with join_table as(
select
*
from customers as c
inner join orders as o
on c.customer_id = o.customer_id;
)

select
*,
rank() over(partition_by customer_id order by order_date desc) as ranked_value
from join_table
where ranked_value = 1;
