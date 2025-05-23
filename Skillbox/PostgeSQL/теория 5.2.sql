select movies.title, Directors.director_name
from movies 
inner join directors
on movies.director_id = directors.director_id ;

select movies.title, Directors.director_name
from movies 
left join directors
on movies.director_id = directors.director_id ;

select movies.title, Directors.director_name
from movies 
right join directors
on movies.director_id = directors.director_id ;

select movies.title, Directors.director_name
from movies 
cross join directors ;

select movies.title, Directors.director_name
from movies 
full outer join directors 
on movies.director_id = directors.director_id ;

select m1.title as movie, m2.title as related_movie
from movies m1
left join movies m2
on m1.related_movie_id = m2.movie_id 
where m2.title is not null;

select movies.title , genres.genre_name
from movies
inner join moviegenres on movies.movie_id = moviegenres.movie_id
inner join genres on moviegenres.genre_id = genres.genre_id ;

select movies.title , genres.genre_name, directors.director_name
from movies
inner join moviegenres on movies.movie_id = moviegenres.movie_id
inner join genres on moviegenres.genre_id = genres.genre_id 
left join moviedirectors on movies.movie_id = moviedirectors.movie_id  
left join directors on moviedirectors.director_id = directors.director_id ;
