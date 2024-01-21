-- Views
select * from customer;

select * from address;

select first_name,last_name,address from customer
inner join address 
on customer.address_id=address.address_id;


create view customer_info as 
select first_name,last_name,address from customer
inner join address 
on customer.address_id=address.address_id;

select * from customer_info;

create or replace view customer_info as 
select first_name,last_name,address,district from customer
inner join address 
on customer.address_id=address.address_id;

select * from customer_info;

drop view if exists customer_info;

-- Alter view
alter view customer_info rename to c_info;

select * from c_info;

drop view c_info;

-- Importing and exporting data


