-- first file
-- second commetn
SELECT tv_genres.name FROM tv_genres JOIN tv_show_genres JOIN tv_shows WHERE tv_shows.title = "Dexter" AND tv_shows.id = tv_show_genres.show_id AND tv_genres.id = tv_show_genres.genre_id ORDER BY tv_genres.name ASC;
