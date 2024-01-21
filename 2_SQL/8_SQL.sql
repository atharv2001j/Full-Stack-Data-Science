-- Update
-- Used to change the value of column
Update account 
set last_login=current_timestamp
where last_login is NULL;

select * from account;


-- reset everything without where condition
Update account 
set last_login=current_timestamp;

select * from account;
select * from account_job;
select * from job;

-- using another table
update account_job
set hire_date=account.created_on
from account
where account_job.user_id=account.user_id;

-- Returning affeced rows
update account
set last_login=current_timestamp
returning user_id,email,created_on;

-- Delete
-- remove rows from table
insert into job
values (2,'cowboy')

delete from job
where job_name='cowboy'
returning job_id,job_name;

-- Alter
create table information
(
info_id serial primary key,
title varchar(73) Not null,
person varchar(58) Not null);

-- renaming the table
alter table information
rename to new_info;

-- rename column
alter table new_info
rename column person to people;

--droping values
insert into new_info
values(1,'some_new_title','atharv');

alter table new_info
alter column people 
drop not null

select * from new_info;

-- drop column
alter table new_info
drop column people;

-- remove dependencies
alter table new_info 
drop column if exists people;

-- Check 

create table employees(
emp_id serial primary key,
first_name varchar(45) not null,
last_name varchar(24) not null,
birthdate Date check(birthdate > '1900-01-01'),
hire_date Date check(hire_date > birthdate),
salary int check(salary > 0)
	)
	
insert into employees values
(
1,
'Atharv',
'Joshi',
'2001-12-19',
'2017-12-24',
2000
)

insert into employees values
(
2,
'Atharv',
'Joshi',
'2001-12-19',
'2017-12-24',
-2000
)

insert into employees values
(
2,
'Dinesh',
'Lokare',
'2001-12-19',
'2017-12-24',
2100
)

select * from employees;







