-- Task 1. Country users
-- Create a table `users` if it does not exist
USE holberton;

-- Create table `users` with attributes `id`, `email`, `name`, and `country`
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
