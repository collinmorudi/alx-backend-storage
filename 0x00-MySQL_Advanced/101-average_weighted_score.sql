-- Script to create a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and stores the average weighted score for all users

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users u
    JOIN (
        SELECT c.user_id,
               SUM(c.score * p.weight) AS total_weighted_score,
               SUM(p.weight) AS total_weight
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        GROUP BY c.user_id
    ) AS weighted_scores
    ON u.id = weighted_scores.user_id
    SET u.average_score = IF(weighted_scores.total_weight > 0, weighted_scores.total_weighted_score / weighted_scores.total_weight, 0);
END//

DELIMITER ;

-- average_weighted_score.sql
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users u
    JOIN (
        SELECT c.user_id,
               SUM(c.score * p.weight) AS total_weighted_score,
               SUM(p.weight) AS total_weight
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        GROUP BY c.user_id
    ) AS weighted_scores
    ON u.id = weighted_scores.user_id
    SET u.average_score = IF(weighted_scores.total_weight > 0, weighted_scores.total_weighted_score / weighted_scores.total_weight, 0);
END//

DELIMITER ;
