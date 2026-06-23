#!/usr/bin/sql
-- 13-change_class.sql
-- Remove all records from second_table with score <= 5

DELETE FROM second_table
WHERE score <= 5;
