-- Напишите запрос, который выберет всех режиссёров, родившихся после 1950 года и имеющих национальность США.

select director_name, birthdate, nationality 
from directors d 
where birthdate > '1950-01-01' and nationality = 'США' ;

-- Напишите запрос, который выберет все фильмы, выпущенные до 2000 года или имеющие продолжительность более 150 минут.

select title, release_year, duration 
from movies m 
where release_year < 2000 or duration > 150 
order by title asc;

-- Напишите запрос, который выберет всех пользователей, не зарегистрированных как администраторы.

select username, is_admin 
from users u 
where not is_admin = true ;

-- Напишите запрос, который выберет все фильмы, выпущенные с 2000 по 2010 год включительно.

select title, release_year 
from movies m 
where release_year between 2000 and 2010;

-- Напишите запрос, который выберет все рецензии, добавленные в октябре.

select review_text, review_date 
from reviews r 
WHERE review_date BETWEEN '2024-10-01 00:00:00' AND '2024-10-31 23:59:59';

-- Напишите запрос, который выберет все фильмы, название которых начинается со слова «Аватар»

select title
from movies
where title like 'Аватар%' ;

-- Напишите запрос, который выберет все фильмы, название которых содержит слово «День».

select title
from movies
where title like '%День%' ;

-- 
select title, release_year, duration, country 
from movies
WHERE release_year > 2010
 AND NOT duration > 140
 AND (duration < 180  OR country = 'Россия');

-- Напишите запрос, который выберет все фильмы, название которых содержит слово «человек» и которые были выпущены в 2010 году или позже.

select title, release_year, duration, country 
from movies
WHERE title like '%человек%'
 AND release_year >= 2010 ;

-- Напишите запрос, который выберет все фильмы, выпущенные с 2010 по 2025 год включительно и в названии которых содержится слово «Уик».

select title, release_year, duration, country 
from movies
WHERE release_year between 2010 and 2025
 AND title like '%Уик%' ;

-- Напишите запрос, который выберет все фильмы, выпущенные до 2000 года, за исключением фильмов продолжительностью от 120 до 130 минут включительно.

select title, release_year, duration, country 
from movies
WHERE release_year > 2010
 AND not duration between 120 and 130;