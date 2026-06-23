#!/usr/bin/sql
-- 16-no_link.sql
-- List all records in second_table where name is not NULL
-- Display score and name, ordered by descending score

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
