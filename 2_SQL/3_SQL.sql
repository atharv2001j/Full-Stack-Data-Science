-- DAY 3
-- Challenge 1
-- how many unique districts are our cusomer from
select Count(Distinct(district)) from address;

-- Challenge 3
-- Retrieve the list of distinct district
select Distinct(district) from address;

-- Challenge 3
-- How many films have a rating of R and a replacement cost between 
-- 5 and 15
select count(title) from film
where rating='R' And ( replacement_cost between 5 and 15);

-- Challenge 3
-- how many films have the word Truman somewhere in title
select count(title) from film where title like '%Truman%';

-- Aggregate functions
select min(replacement_cost) from film;

select max(replacement_cost) from film;

select avg(replacement_cost) from film;

select Max(replacement_cost),min(replacement_cost) from film;

select round(avg(replacement_cost),2) from film;

select round(avg(replacement_cost),4) from film;

select sum(replacement_cost) from film;

-- Group by
select customer_id from payment
group by customer_id
order by customer_id;

select customer_id,sum(amount) from payment
group by customer_id;

select customer_id,sum(amount) from payment
group by customer_id
order by sum(amount) DESC;

select customer_id,staff_id,sum(amount) from payment
group by staff_id,customer_id;

select customer_id,staff_id,sum(amount) from payment
group by staff_id,customer_id
order by customer_id;

select Date(payment_date),sum(amount)
from payment
group by date(payment_date);

select date(payment_date),sum(amount) from payment
group by payment_date
order by sum(amount) DESC;


-- Challenge 1
select staff_id,count(amount)from payment
group by staff_id
order by count(amount ) DESC;

-- Challenge 2
-- what is average replacement cost per rating
select rating,avg(replacement_cost) from film
group by rating 
order by avg(replacement_cost) ASC;

-- challenge 3
-- Top 5 customer by total spend
select customer_id,sum(amount) from payment
group by customer_id
order by sum(amount) desc limit 5;

-- having
-- when we use aggregate function 
select customer_id ,sum(amount)from payment
group by customer_id
having sum(amount)>100;

select store_id,count(customer_id)
from customer
group by store_id;

select store_id,count(*)
from customer
group by store_id;

select store_id,count(customer_id)
from customer
group by store_id
having count(customer_id)>300;

select store_id,count(*)
from customer
group by store_id
having count(*)>300;

--Challenge 1
-- count the customer id having transaction greater than equal to 40
select customer_id,count(*) from payment
group by customer_id
having count(*)>=40;

-- Challenge 2
select * from payment;

select customer_id, sum(amount)
from payment
where staff_id=2
group by customer_id
having sum(amount)>100 ;

-- Test 1
-- Q1. Return the customer ids of customer who have spend at least 
-- 110 with staff member who has id of 2
select customer_id, sum(amount)
from payment
where staff_id=2
group by customer_id
having sum(amount)>=110 ;

-- Q2. how many films begin with the letter J
select count(title) from film
where title like 'J%';

-- Q3 what customer has the highest customer id number whose name
-- starts with an E and has address id lower than 500?

select * from customer;

select first_name,last_name  from customer
where first_name like 'E%' and address_id<500 
order by customer_id desc
limit 1;




