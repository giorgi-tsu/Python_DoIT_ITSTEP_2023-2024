use it_step;

select city, phone, CustomerName  from customers group by city;
select city,  phone, sum(creditLimit) from customers group by city, phone order by city;

select * from customers order by city;

SELECT city, sum(creditLimit) FROM it_step.customers group by city order by city;
SELECT city, count(*) FROM it_step.customers group by city order by city;

SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode, 'ONLY_FULL_GROUP_BY', ""));



/* select count(customerNumber) as TotalCustomers from customers group by city order by city; */

SELECT country FROM it_step.customers group by city order by city;

SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));

select city, country, count(*) as poplation from customers group by city order by city;

Error Code: 1055. Expression #2 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'it_step.customers.phone' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by

select country, creditLimit as countryCredit from customers group by country order by country;

select city, country, sum(creditLimit) from customers where creditLimit > 22000 group by city;


