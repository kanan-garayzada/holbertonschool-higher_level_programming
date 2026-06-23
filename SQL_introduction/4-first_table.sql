#!/usr/bin/sql
-- 4-first_table.sql
-- Create table first_table with id INT and name VARCHAR(256) if it does not exist
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
