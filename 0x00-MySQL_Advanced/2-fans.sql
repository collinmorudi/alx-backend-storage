-- Script to rank country origins of bands by the number of (non-unique) fans

-- Import the metal_bands table dump
SOURCE metal_bands.sql;

-- Select and rank the country origins by number of fans
SELECT origin, SUM(nb_fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
