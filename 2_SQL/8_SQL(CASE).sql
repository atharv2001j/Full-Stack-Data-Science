select * from customer;

select customer_id,
case
when customer_id<100  then 'Premium'
when customer_id between 101 and 200 then 'plus'
else 'Normal'
END

from customer;

select customer_id,
case customer_id
when 2 then 'winner'
when 5 then 'Second Place'
else 'Normal'
End as raffle_result
from customer;

select * from film;

select rental_rate from film;

select 
case rental_rate
when 0.99 then 1
else 0
end 
from film;

select 
sum(case rental_rate
when 0.99 then 1
else 0
end ) as number_of_bargens
from film;

select 
sum(case rental_rate
when 0.99 then 1
else 0
end ) as bargens,
sum(case rental_rate
	when 2.99 then 1
	else 0
	end) as regular
from film;

select 
sum(case rental_rate
when 0.99 then 1
else 0
end ) as bargens,
sum(case rental_rate
	when 2.99 then 1
	else 0
	end) as regular,
sum(case rental_rate
   when 4.99 then 1
   else 0
   end) as premium
from film;


