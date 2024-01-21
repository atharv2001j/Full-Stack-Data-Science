-- importing and exporting
Create table Simple(
a int,
b int,
c int
)

select * from Simple;

--- Exporting a table 

-----------------------------------------------------------------
create table contries(
contry_ID varchar(16),
country_name varchar(67),
region_id decimal(10,0)
)

select * from contries;

-----------------------------------------------------
create table dup_contries as 
(
select * from contries)
with no data;

create table if not exists countries
(
country_id varchar(67) not null,
country_name varchar(67) not null,
region_id decimal(10,0) not null
)

-- write a sql statement to creae table job with columns and check whether 
-- the max_salary exceed the the upper limit 25000

create table job(
job_id varchar(15),
job_title varchar(67),
min_salary varchar(45),
max_salary int check(max_salary > 25000)
)

-- write a sql query to create contry table and make sure that no contries except
-- Italy,India,china willbe entered in the table

drop table contries;

create table contries
(
contry_id varchar(15) not null,
contry_name varchar(45) check(contry_name not in ('Italy','India','China')),
region_id decimal(10,0)	
	)
-- make sure that no duplicate entries against column country
create table contries
(
country_id int unique,
country_name varchar(56),
region_id decimal(10,0)
)

----------
drop table job;

create table job
(
job_id int unique,
job_title varchar(56) default 0,
min_salary int check(min_salary=8000),
max_salary int Null);

-----------

create table countries
(
country_id int primary key,
country_name varchar(56) not null,
region_id decimal(10,0) not null
)

----------------

create table countries
(
country_id int unique auto_increment,
country_name varchar(56) not null,
region_id decimal(10,0) not null
)

-----------
create table countries
(
country_id int unique auto_increment,
country_name varchar(56) not null,
region_id decimal(10,0) not null,
primary key(country_id,region_id)
)

----------
create table job_history(
employee_id int not null primary key,
start_date date not null,
end_date date not null,
job_id varchar(67) not null,
department_id decimal(10,0) not null,
foreign key(job_id) references job(job_id)
)






