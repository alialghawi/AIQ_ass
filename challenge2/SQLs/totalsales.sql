-- SQLite
SELECT user_id, SUM(value) AS total_sales 
FROM orders
GROUP BY user_id
ORDER BY total_sales DESC;
