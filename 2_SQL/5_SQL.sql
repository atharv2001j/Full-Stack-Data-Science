-- Mathematical Functions
--1) Division
select rental_rate/replacement_cost from film;

-- 2)Addition
select rental_rate+replacement_cost from film;

-- 3) Subtraction
select rental_rate-replacement_cost from film;

-- 4) Multiplication
select rental_rate*replacement_cost from film;

-- 5)Modulo
select rental_rate%replacement_cost from film;

-- 6) Exponentiation
select rental_rate^replacement_cost from film;

-- 7) Square root
select |/rental_rate from film;

-- 8) Cube root
select ||/replacement_cost from film;

-- 9)Facorial
select factorial(replacement_cost) from film;

-- 10) Round
select round(replacement_cost,2) from film;

-- 11) Percentage
select round(replacement_cost,2)*100 from film;

-- 12) As
select round(rental_rate/replacement_cost,4) as percentage_cost from film;

select 0.1 * replacement_cost as deposit
from film;

-- Functions
select * from customer;

select length(first_name) from customer;

select first_name || last_name from customer;

select first_name ||' ' ||last_name as Full_name from customer;

select upper(first_name || ' ' || upper(last_name)) as Full_name 
from customer;

select left(first_name,1) || last_name || '@gmail.com' from customer;

select right(first_name,1) || last_name || '@gmail.com' from customer;

select upper(right(first_name,1) || last_name || '@gmail.com') from customer;

select lower(right(first_name,1) || last_name || '@gmail.com') from customer;

select lower(right(first_name,1) || last_name || '@gmail.com') 
as customer_email from customer;

-- Subquery
select * from film;

select Avg(rental_rate) from film;

select title , rental_rate
from film
where rental_rate>(select avg(rental_rate) from film)

select * from rental;
select * from inventory;

select * from rental
where return_date between '2005-05-29' and '2005-05-30';

select inventory.film_id
from rental
inner join
inventory on
inventory.inventory_id=rental.inventory_id
where return_date between '2005-05-29' and '2005-05-30';

select film_id ,title
from film where
film_id in
(
select inventory.film_id
from rental
inner join
inventory on
inventory.inventory_id=rental.inventory_id
where return_date between '2005-05-29' and '2005-05-30'

)



