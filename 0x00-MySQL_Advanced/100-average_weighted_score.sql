-- Script to create a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and stores the average weighted score for a user

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight INT;
    DECLARE average_score FLOAT;

    -- Calculate the total weighted score and total weight
    SELECT SUM(c.score * p.weight), SUM(p.weight)
    INTO total_weighted_score, total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Check if total weight is not zero to avoid division by zero
    IF total_weight > 0 THEN
        SET average_score = total_weighted_score / total_weight;
    ELSE
        SET average_score = 0;
    END IF;

    -- Update the average_score in the users table
    UPDATE users
    SET average_score = average_score
    WHERE id = user_id;
END//

DELIMITER ;

-- 100-average_weighted_score.sql
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight INT;
    DECLARE average_score FLOAT;

    SELECT SUM(c.score * p.weight), SUM(p.weight)
    INTO total_weighted_score, total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    IF total_weight > 0 THEN
        SET average_score = total_weighted_score / total_weight;
    ELSE
        SET average_score = 0;
    END IF;

    UPDATE users
    SET average_score = average_score
    WHERE id = user_id;
END//

DELIMITER ;
