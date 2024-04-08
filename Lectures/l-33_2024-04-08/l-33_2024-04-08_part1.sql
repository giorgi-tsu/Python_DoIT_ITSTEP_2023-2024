use it_step;

select * from customers;

select count(*) as total_customers from customers;

select	sum(creditLimit) as totalCreditLimit from customers;

select	avg(creditLimit) as avgCreditLimit from customers;

select	min(creditLimit) as minCreditLimit from customers;

select	max(creditLimit) as maxCreditLimit from customers;