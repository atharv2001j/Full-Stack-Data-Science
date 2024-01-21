-- 1.How can you retrieve all the information from the cd.facilities table?
select * from cd.facilities;

-- 2.You want to print out a list of all of the facilities and their cost to members. 
-- How would you retrieve a list of only facility names and costs?

select name,membercost from cd.facilities;

--3.How can you produce a list of facilities that charge a fee to members?
select * from cd.facilities 
where membercost <> 0;

-- 4.How can you produce a list of facilities that charge a fee to members, and that fee is less than 1/50th of the monthly maintenance cost? Return the facid, facility name,
--member cost, and monthly maintenance of the facilities in question
select facid,name,membercost,facilities.monthlymaintenance
from cd.facilities
where membercost <> 0 and membercost < (monthlymaintenance)/50;

-- 5.	How can you produce a list of all facilities with the
-- word 'Tennis' in their name?

select * from cd.facilities
where name like '%Tennis%';

-- 6.	How can you retrieve the details of facilities with ID 1 and 5? Try to do it 
-- without using the OR operator.
select * from cd.facilities 
where facid in (1,5);

--7.How can you produce a list of members who joined 
-- after the start of September 2012? Return the memid, 
-- surname, firstname, and joindate of the members in question.
select * from cd.members
select memid,surname,firstname,joindate from cd.members
where extract(year from joindate)>=2012 and extract(month from joindate)>=9;

-- 8.	How can you produce an ordered list of the first 10 
-- surnames in the members table? The list must not contain duplicates.
select distinct(surname) from cd.members
order by surname
limit 10;

-- 9.	You'd like to get the signup date of your last member. 
-- How can you retrieve this information?
select joindate 
from cd.members
order by joindate desc
limit 1;

-- 10.Produce a count of the number of facilities 
-- that have a cost to guests of 10 or more.
select count(*)
from cd.facilities
where guestcost>=10;

--11.	Produce a list of the total number of slots booked per 
--facility in the month of September 2012. Produce an output 
--table consisting of 
--facility id and slots, sorted by the number of slots.
select * from cd.bookings;
select count(slots),facid
from cd.bookings
where extract(month from starttime)=9 and extract(year from starttime)=2012
group by facid
order by facid desc;

-- 12.	Produce a list of facilities with more than 
-- 1000 slots booked. Produce an output table consisting of facility id 
--and total slots, sorted by facility id.
select facid ,sum(slots) as total_cost
from cd.bookings
group by facid
having sum(slots)>1000;

-- 13.	How can you produce a list of the start times for 
--bookings for tennis courts, for the date '2012-09-21'? Return a list 
--of start time and facility name pairings, ordered by the time
select starttime,name
from cd.bookings as b
join 
cd.facilities as f
on
b.facid=f.facid
where f.facid in (0,1) and starttime>='2012-09-21' and starttime<='2012-09-22'
order by b.starttime;

-- 14.	How can you produce a list of the start times for 
--bookings by members named 'David Farrell'?
select * from cd.members
select starttime from cd.bookings as b
join cd.members as m
on b.memid=m.memid
where m.firstname='David' and m.surname='Farrell';
