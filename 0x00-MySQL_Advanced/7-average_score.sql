-- Script to create a stored procedure ComputeAverageScoreForUser
-- that computes and stores the average score for a user

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_projects INT;
    DECLARE average_score FLOAT;

    -- Calculate the total score and total number of projects
    SELECT SUM(c.score), COUNT(c.project_id)
    INTO total_score, total_projects
    FROM corrections c
    WHERE c.user_id = user_id;

    -- Check if total number of projects is not zero to avoid division by zero
    IF total_projects > 0 THEN
        SET average_score = total_score / total_projects;
    ELSE
        SET average_score = 0;
    END IF;

    -- Update the average_score in the users table
    UPDATE users
    SET average_score = average_score
    WHERE id = user_id;
END//

DELIMITER ;

-- average_score.sql
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_projects INT;
    DECLARE average_score FLOAT;

    SELECT SUM(c.score), COUNT(c.project_id)
    INTO total_score, total_projects
    FROM corrections c
    WHERE c.user_id = user_id;

    IF total_projects > 0 THEN
        SET average_score = total_score / total_projects;
    ELSE
        SET average_score = 0;
    END IF;

    UPDATE users
    SET average_score = average_score
    WHERE id = user_id;
END//

DELIMITER ;
