create table account(
user_id serial primary key,
username varchar(16) unique not null,
password varchar(18) Not Null,
email varchar(17) unique not null,
created_on timestamp not null,
last_login timestamp not null
)

create table job
(
job_id serial primary key,
job_name varchar(16) unique not null
)

create table account_job
(
user_id int references account(user_id),
job_id int references job(job_id),
hire_date Timestamp
)

insert into account values
(
1,'atharv','atharv@2001','jo67@gmail.com',current_timestamp,current_timestamp
);

select * from account;

insert into job values
(
1,'software engg'
)

insert into account_job values
(
1,1,current_timestamp
)


