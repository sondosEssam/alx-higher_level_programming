-- first file
-- second commetn

USE hbtn_0d_usa;
SELECT cities.id , cities.name FROM cities RIGHT JOIN states ON cities.state_id = states.id WHERE states.name = "California"
