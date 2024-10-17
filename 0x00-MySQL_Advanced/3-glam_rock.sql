-- Script to list Glam rock bands ranked by their longevity

SELECT band_name,
       IFNULL(2022 - formed, 2022 - split) AS lifespan
FROM metal_bands
WHERE genre = 'Glam rock'
ORDER BY lifespan DESC;

SELECT band_name,
       IF(split IS NULL, 2022 - formed, split - formed) AS lifespan
FROM metal_bands
WHERE genre = 'Glam rock'
ORDER BY lifespan DESC;
