-- 1). Write a SQL statement to create a table named jobs including 
-- columns job_id, job_title, min_salary, max_salary and check whether the 
-- max_salary amount exceeding the upper limit 25000.
create table jobs(
	job_id int primary key,
	job_title varchar(45),
	min_salary int ,
	max_salary int check(max_salary>=25000),
	email varchar(67)
)

-- 2)Write a SQL statement to change the email column 
-- of the jobs table with 'not available' for all employees.

UPDATE jobs
SET email = 'not available';
 
-- Q3. Write a SQL statement to rename the table jobs to jobs_new.

ALTER TABLE jobs RENAME TO jobs_new;

-- Q.4 Write a SQL statement to add a 
-- column dept_id to the table locations.
ALTER TABLE locations
ADD dept_id INT;

-- Q.5 Write a SQL statement to insert a record with your 
--own value
-- into the table jobs_new against each column

insert into jobs_new (job_id, job_title, min_salary, max_salary)
values (1, 'Software Engineer', 60000, 120000);

-- Q.6 Write a query to display the names (job_id,dept_id) .

select job_id,dept_id from job 

-- Q.7 Write a query to get the maximum total salaries payable 
-- to employees.

select max(salary)
from employees;

-- Q.8 Write a query to get the average salary 
-- and number of employees are working.

select avg(salary),count(emp_id)
from employees;

--Q.9 Create a table manager_details comprises of 
--manager_id,manager_name ,dept_id and Write a query to 
--make a join with 
--two tables jobs_new and manager_details

create table manager_details(
manager_id int primary key,
manager_name varchar(45),
dept_id int );

select *,manager_details.manager_name 
from jobs_new 
inner join manager_details on
jobs_new.dept_id=manager_details.dept_id;

-- Q.10 Write a SQL subquery to find the emp_id  of all employees  
-- from jobs_new table who works in the IT department.

select dept_id
from jobs_new
where dept_id in (select dept_id from manager_details where dept_name ='IT');









