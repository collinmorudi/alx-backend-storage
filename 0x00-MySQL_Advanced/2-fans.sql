-- Script to rank country origins of bands by the number of (non-unique) fans

SELECT origin, nb_fans,
       DENSE_RANK() OVER (ORDER BY nb_fans DESC) AS rank
FROM metal_bands
ORDER BY nb_fans DESC;

-- fans.sql
SELECT origin, nb_fans,
       DENSE_RANK() OVER (ORDER BY nb_fans DESC) AS rank
FROM metal_bands
ORDER BY nb_fans DESC;
