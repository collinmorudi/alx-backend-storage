-- commends will be added soon

ALTER TABLE names ADD first_letter CHAR(1);

UPDATE names SET first_letter = LEFT(name, 1);

CREATE INDEX idx_name_first_score ON names (first_letter, score);

-- index_name_score.sql
ALTER TABLE names ADD first_letter CHAR(1);
UPDATE names SET first_letter = LEFT(name, 1);
CREATE INDEX idx_name_first_score ON names (first_letter, score);

