#!/usr/bin/sql
-- 10-top_score.sql
-- List all records from second_table with score and name, ordered by score descending

SELECT score, name
FROM second_table
ORDER BY score DESC;
