-- Script to create the users table with attributes id, email, name, and country.
-- The table will store user information with a unique email and predefined countries.

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);

-- The table contains:
-- - id: Integer, auto-increment, primary key, not null
-- - email: String, max 255 characters, not null, unique
-- - name: String, max 255 characters
-- - country: Enumeration (US, CO, TN), not null, default 'US'
