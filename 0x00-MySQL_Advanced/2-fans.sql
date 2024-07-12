-- SQL script to rank country origins of bands by the number of fans

-- Select the origin (country) and count of fans from the bands table
SELECT origin, COUNT(*) as nb_fans
FROM bands
-- Join with another relevant table if needed
GROUP BY origin
-- Order by number of fans in descending order
ORDER BY nb_fans DESC;
