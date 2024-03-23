-- SQLite
 -- Table for user data
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username VARCHAR2(50) NOT NULL, 
    age INTEGER,
    country VARCHAR2(50)
);

-- Table for order data
CREATE TABLE orders (
    timestamp TIMESTAMP,
    user_id INTEGER,
    value NUMBER,
    PRIMARY KEY (timestamp, user_id), -- Assuming orders are unique based on time and user
    FOREIGN KEY (user_id) REFERENCES users(id) 
);
