-- Alises ( AS)
-- It will give temporary name to the column
select amount as rental_price 
from payment;

select count(amount) AS num_transactions
from payment;

select customer_id,sum(amount)
from payment
group by  customer_id;

select customer_id,sum(amount) AS total_spent
from payment
group by  customer_id;

select customer_id,sum(amount) 
from payment
group by  customer_id
having sum(amount)>100;

select customer_id,sum(amount) as total_spent
from payment
group by  customer_id
having sum(amount)>100;

select customer_id,sum(amount) as total_spent
from payment
group by  customer_id
having total_spent>100;
--ERROR:  column "total_spent" does not exist
-- LINE 4: having total_spent>100;

select customer_id,amount as new_name
from payment
where amount > 2;

-- Join
-- It allow us to join multiple columns
select * from customer;
select * from payment;

-- Types of Join
-- 1) Inner Join
select * from customer 
inner join payment
on customer.customer_id=payment.customer_id;

select payment.payment_id ,payment.customer_id,customer.first_name
from payment
inner join customer
on payment.customer_id = customer.customer_id;

-- 2) Full outer join

select * from customer 
full outer join payment
on customer.customer_id=payment.customer_id
where customer.customer_id IS Null
Or payment.customer_id is null;

--a) left outer join
select film.film_id,title,inventory_id,store_id
from film
left join inventory on
inventory.film_id=film.film_id;

select film.film_id,film.title,inventory.inventory_id,inventory.store_id
from film
left outer join inventory
on
film.film_id=inventory.film_id
where inventory.film_id is null;

-- 2) Right Outer Join
-- same as LJ but tables are switched


-- Challenge 1
-- email of california
select customer.email from customer
inner join address
on customer.address_id=address.address_id
where address.district='California' ;

select customer.email from customer
inner join address
on customer.address_id=address.address_id
where address.district='Alberta' ;

-- Challenge 2
select * from film;
select * from actor;
select * from film_actor;

select title,first_name,last_name from actor
inner join  film_actor
on actor.actor_id=film_actor.actor_id
inner join film
on film_actor.film_id=film.film_id
where first_name='Nick' and last_name='Wahlberg';


-- Advanced SQL Topics
show all

show Timezone

select now()

select timeofday()

select current_date

-- 1) Extract()
select extract(year from payment_date) as myyear
from payment;

select extract(month from payment_date) as mymonth
from payment;

select extract(quarter from payment_date) as pay_month
from payment;

-- 2) Age
select age(payment_date) from payment;

-- 3) To_char
select to_char(payment_date,' mm/dd/yyyy')
from payment;

-- Challenge 1
-- month in which you have do payment
select distinct(To_char(payment_date,'month')) from payment

-- Challenge 2
-- how many payments occures on a monday
select count(*)
from payment
where extract(dow from payment_date)=1;
