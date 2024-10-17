-- 3-glam_rock.sql

SELECT band_name, 
       IFNULL(2022 - formed, 2022 - split) AS lifespan
FROM metal_bands
WHERE genre = 'Glam rock'
ORDER BY lifespan DESC;
