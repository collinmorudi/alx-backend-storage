-- Script to list Glam rock bands ranked by their longevity

-- Import the metal_bands table dump
SOURCE metal_bands.sql;

-- Select and rank Glam rock bands by their lifespan
SELECT
    band_name,
    CASE
        WHEN split IS NULL THEN 2022 - formed
        ELSE split - formed
    END AS lifespan
FROM
    metal_bands
WHERE
    main_style = 'Glam rock'
ORDER BY
    lifespan DESC;
