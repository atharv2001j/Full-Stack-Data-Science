Select * from film

select * from actor;

select * from city;

select count(category_id) from film_category;

select max(amount) from payment;

select * from payment;

-- atharv Joshi
/*
atharv joshi
*/

select first_name,last_name from actor where first_name='Nick' AND last_name='Wahiberg';

select * from film_category where category_id=6;

select * from language where name='English';

select * from address where district='QLD';

select * from actor;

select * from address;

select * from film;

select distinct release_year from film;

select * from film_category;

select * from customer;

select rating from film;

select distinct(rating) from film;

select count(first_name) from actor;

select count(*) from payment;

select amount from payment;

select distinct amount from payment;

select count(distinct amount) from payment;

select first_name from actor where first_name='Nick';

select first_name ,last_name from customer where first_name='Mary' AND last_name='Ely';

select * from film;

select * from film where title='Airport Pollock'

