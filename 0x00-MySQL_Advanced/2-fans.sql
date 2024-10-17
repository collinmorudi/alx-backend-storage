-- Select the origin of the band and the total number of fans
-- Then group the results by origin and sum the number of fans per origin
-- Finally, order the results by the total number of fans in descending order

SELECT origin, SUM(nb_fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

