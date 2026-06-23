#!/usr/bin/sql
-- 15-groups.sql
-- List the number of records for each score in second_table

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
