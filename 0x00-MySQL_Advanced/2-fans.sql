-- 2-fans.sql

-- Create a temporary table to store the results
CREATE TEMPORARY TABLE IF NOT EXISTS band_fans AS
SELECT origin, COUNT(*) AS nb_fans
FROM metal_bands
GROUP BY origin;

-- Select the origins and their corresponding fan counts, ordered by nb_fans
SELECT origin, SUM(nb_fans) AS nb_fans
FROM band_fans
GROUP BY origin
ORDER BY nb_fans DESC;
