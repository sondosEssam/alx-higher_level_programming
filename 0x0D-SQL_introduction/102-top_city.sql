-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT city, avg(value) AS avg_temp FROM temperatures WHERE month = 7 or month = 8 ORDER BY value DESC ;
