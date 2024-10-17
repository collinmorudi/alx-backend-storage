-- Script to create the users table
-- The table will store user information with unique email addresses

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);

-- The table contains:
-- - id: Integer, auto-increment, primary key, not null
-- - email: String, max 255 characters, not null, unique
-- - name: String, max 255 characters
