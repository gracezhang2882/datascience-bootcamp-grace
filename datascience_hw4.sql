CREATE TABLE CUSTOMERS (
  customer_id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  Address TEXT
);

CREATE TABLE ITEMS (
  item_id INTEGER PRIMARY KEY,
  item_name TEXT,
  price REAL,
  department TEXT
);

CREATE TABLE SALES (
  Date TEXT,
  Order_id INTEGER,
  Item_id INTEGER,
  Customer_id INTEGER,
  Quantity INTEGER,
  Revenue REAL,
  FOREIGN KEY (Item_id) REFERENCES ITEMS(item_id),
  FOREIGN KEY (Customer_id) REFERENCES CUSTOMERS(customer_id)
);


INSERT INTO CUSTOMERS VALUES 
  (1, 'John', 'Doe', '123 Main St'),
  (2, 'Jane', 'Smith', '456 Park Ave'),
  (3, 'Alice', 'Lee', '789 Broadway');

INSERT INTO ITEMS VALUES 
  (101, 'Notebook', 10.0, 'Stationery'),
  (102, 'Pen', 2.0, 'Stationery'),
  (103, 'Laptop', 800.0, 'Electronics'),
  (104, 'Mouse', 25.0, 'Electronics'),
  (105, 'T-shirt', 15.0, 'Clothing');

INSERT INTO SALES VALUES 
  ('2023-03-18', 1001, 101, 1, 2, 20.0),
  ('2023-03-18', 1002, 103, 2, 1, 800.0),
  ('2023-03-18', 1003, 102, 1, 5, 10.0),
  ('2023-01-10', 1004, 104, 3, 2, 50.0),
  ('2023-01-15', 1005, 105, 3, 4, 60.0),
  ('2022-07-01', 1006, 101, 2, 1, 10.0),
  ('2022-08-10', 1007, 105, 3, 2, 30.0);


SELECT COUNT(DISTINCT Order_id) AS total_orders_18_mar_2023
FROM SALES
WHERE Date = '2023-03-18';

SELECT COUNT(DISTINCT S.Order_id) AS john_doe_orders
FROM SALES S
JOIN CUSTOMERS C ON S.Customer_id = C.customer_id
WHERE Date = '2023-03-18'
  AND C.first_name = 'John'
  AND C.last_name = 'Doe';

SELECT COUNT(DISTINCT Customer_id) AS total_customers_jan_2023,
       AVG(customer_total) AS avg_spend_per_customer
FROM (
    SELECT Customer_id, SUM(Revenue) AS customer_total
    FROM SALES
    WHERE Date BETWEEN '2023-01-01' AND '2023-01-31'
    GROUP BY Customer_id
) AS customer_spending;

SELECT I.department, SUM(S.Revenue) AS total_revenue
FROM SALES S
JOIN ITEMS I ON S.Item_id = I.Item_id
WHERE substr(Date, 1, 4) = '2022'
GROUP BY I.department
HAVING total_revenue < 600;

SELECT Order_id, SUM(Revenue) AS order_revenue
FROM SALES
GROUP BY Order_id
ORDER BY order_revenue DESC
LIMIT 1;

SELECT Order_id, SUM(Revenue) AS order_revenue
FROM SALES
GROUP BY Order_id
ORDER BY order_revenue ASC
LIMIT 1;

WITH OrderRevenue AS (
    SELECT Order_id, SUM(Revenue) AS total_revenue
    FROM SALES
    GROUP BY Order_id
    ORDER BY total_revenue DESC
    LIMIT 1
)
SELECT S.Order_id, I.Item_name, S.Quantity, S.Revenue
FROM SALES S
JOIN ITEMS I ON S.Item_id = I.Item_id
WHERE S.Order_id = (SELECT Order_id FROM OrderRevenue);
