-- first file
-- second commetn
SELECT cities.id , cities.name , states.name FROM cities RIGHT JOIN states ON cities.state_id = states.id ORDER BY cities.id;
