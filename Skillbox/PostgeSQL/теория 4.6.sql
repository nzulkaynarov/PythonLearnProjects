-- union объединяет выборку исключая дупликаты
select director_name as name from directors d 
union
select actor_name as name from actors a ;

-- union объединяет выборку не исключая дупликаты, т.е. добавляя первое со вторым
select director_name as name from directors d 
union all
select actor_name as name from actors a ;

-- union показывает те записи, которые присутствуют в двух выборках
select director_name as name from directors d 
intersect
select actor_name as name from actors a ;

-- union показывает те записи, которые во второй выборке
select director_name as name from directors d 
except
select actor_name as name from actors a ;

select title, duration
from movies m 
where duration >= 120
union 
select title, release_year
from movies m2
where release_year > 2000;