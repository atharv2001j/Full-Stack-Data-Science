
create table students(student_id int primary key,
					 first_name varchar(68),
					 last_name varchar(48),
					 homeroom_number int ,
					 phone varchar(20) unique,
					 email varchar(20) unique
			)

create table teachers(
	teacher_id int primary key,
	first_name varchar(78),
	last_name varchar(56),
	homeroom_numbers int ,
	deparment varchar(54),
	email varchar(45) unique,
	phone varchar(64) unique
	
)

insert into students values
(
1,'Rahul','Galande',5,'7775551234','Rahul@gmail.com')

insert into teachers values 
(
1,'Chandrashekhar','Gogte',5,'Biology','Chandrashekhar.Gogte@gmail.com','7775554221')

select * from students;
select * from teachers;

alter table students add column
graduation_year int;

alter table students 
drop column graduation_year;

delete from students 
where student_id=1;

alter table students
rename to stud;













