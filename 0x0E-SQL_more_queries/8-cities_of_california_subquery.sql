-- first file
-- second commetn
SELECT cities.id , cities.name FROM cities RIGHT JOIN states ON cities.state_id = states.id WHERE states.name = "California" ORDER BY cities.id ASC;
