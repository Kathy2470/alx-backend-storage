-- Task 0. We are all unique!
-- Create a table `users` if it does not exist
USE holberton;

-- Create table `users` with unique `email` constraint
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);

-- End of SQL script
