-- Rank country origins of bands by number of fans

CREATE TEMPORARY TABLE temp_band_fans AS
SELECT
    origin,
    SUM(nb_fans) AS total_fans
FROM
    metal_bands
GROUP BY
    origin;

SELECT
    origin,
    total_fans AS nb_fans
FROM
    temp_band_fans
ORDER BY
    total_fans DESC;
