-- 3-glam_rock.sql

SELECT b.band_name,
       IFNULL(2022 - b.formed, 2022 - b.split) AS lifespan
FROM metal_bands b
WHERE LIKE '%Glam rock%'
ORDER BY lifespan DESC;
