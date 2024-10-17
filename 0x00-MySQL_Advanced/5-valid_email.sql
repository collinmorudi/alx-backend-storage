-- Script to create a trigger that resets valid_email when email is changed

-- Initial setup
DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    valid_email BOOLEAN NOT NULL DEFAULT 0,
    PRIMARY KEY (id)
);

INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");
INSERT INTO users (email, name, valid_email) VALUES ("sylvie@dylan.com", "Sylvie", 1);
INSERT INTO users (email, name, valid_email) VALUES ("jeanne@dylan.com", "Jeanne", 1);

-- Create the trigger
DELIMITER //

CREATE TRIGGER before_users_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END //

DELIMITER ;

-- Show users and update (or not) email
SELECT * FROM users;
UPDATE users SET valid_email = 1 WHERE email = "bob@dylan.com";
UPDATE users SET email = "sylvie+new@dylan.com" WHERE email = "sylvie@dylan.com";
UPDATE users SET name = "Jannis" WHERE email = "jeanne@dylan.com";
SELECT "--";
SELECT * FROM users;
UPDATE users SET email = "bob@dylan.com" WHERE email = "bob@dylan.com";
SELECT "--";
SELECT * FROM users;
