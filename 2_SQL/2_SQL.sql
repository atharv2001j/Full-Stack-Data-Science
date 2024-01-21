select * from film
where rental_rate > 4 AND replacement_cost >=19.99
AND rating='R';

select count(*) from film
where rental_rate > 4 AND replacement_cost >=19.99
AND rating='R';

select count(title) from film
where rental_rate > 4 AND replacement_cost >=19.99
AND rating='R';

select count(*) from film
where rating='R' OR rating='PG-13'

select * from film
where rating !='R';

select count(*) from film
where rating !='R';

select count(*) from film
where rating <>'R';
-- Challenge 1:
-- Find out the email where the name is Nancy Thomas
select email from Customer
where first_name='Nancy' AND last_name='Thomas';

-- Challenge 2
-- description for the movie 'Outlaw Hanky'
select description from film
where title='Outlaw Hanky';

-- Challenge 3
-- Get a phone number  for y=the customer who live at '259 Ipoh Drive'
select phone from address
where address='259 Ipoh Drive';


-- Order by
select * from customer Order by customer_id DESC

select * from customer 
order by first_name ASC;

select * from customer 
order by first_name desc;

select * from customer 
order by store_id desc;

select store_id,first_name,last_name from customer 
order by store_id ,first_name desc;

select store_id,first_name,last_name from customer 
order by store_id ASC ,first_name desc;

--Limit command
-- allow us to limit the number of rows returned for the query
select * from payment
order by payment_date DESC
limit 5;

select * from payment
where amount<>0 
order by payment_date
limit 5;

--Challenge 1
-- customer id of first 10 customer
select customer_id
from payment
order by payment_date
limit 10;

-- challenge 2
-- a customer wants to quickly rent a video to watch over therir short
-- lunch break.what are the titile of 5 shortest movies
select title from film
order by length
limit 5;

-- challenge 3
-- how much movies are with 50 min time period 
select count(title) from film
where length<=50;


-- Between Operator
-- match value against range

select amount from payment  
where amount between 8 and 9 limit 4;

select amount from payment  
where amount not between 8 and 9 limit 4;

select COUNT(amount) from payment  
where amount between 8 and 9 ;

select COUNT(amount) from payment  
where amount NOT between 8 and 9 ;

select * from payment 
where payment_date between
'2007-02-01' and '2007-02-15';

--in operator
-- to check the presence of value
select * from payment 
where amount in (0.99,1.98,1.99);

select count(*) from payment 
where amount in (0.99,1.98,1.99);

select count(*) from payment 
where amount not in (0.99,1.98,1.99);

select * from customer
where first_name 
in('john','jake','Julie');

select * from customer
where first_name 
not in('john','jake','Julie');

--like Operator(%)
-- This operator used to matching pattern 
select title from film
where title like 'Mission Impossible_';

select * from film
where title like 'Ali Foreve_';

select * from customer 
where first_name like 'J%';

select count(*) from customer 
where first_name like 'J%';

select * from customer 
where first_name like 'J%' AND last_name like 'S%';

-- Case Sensitive
select * from customer 
where first_name like 'j%' AND last_name like 's%';

-- ilike operator
select * from customer 
where first_name ilike 'j%' AND last_name ilike 's%';

select * from customer
where first_name like '%er%';

select * from customer
where first_name like '%her%';

select * from customer
where first_name like '_her%';

select * from customer
where first_name like 'A%';

select * from customer
where first_name like 'A%'
order by last_name;

select * from customer
where first_name like '%er%' AND last_name not like 'B%'
order by last_name;

--Challenge 1
-- Payments greater than $5.00
select count(*) from payment
where amount>5.00;

-- challenge 2
--actor name starts with p
select count(*) from actor
where first_name like 'P%';









