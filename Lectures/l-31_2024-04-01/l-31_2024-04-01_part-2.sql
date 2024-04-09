use it_step;

select * from customers;

select customerName, city from customers;

select * from customers limit 5;

select * from customers where city = "NYC";
	
select * from customers where city != "NYC";

select customerName, creditLimit from customers where creditLimit > 23000;

select customerName, creditLimit from customers where creditLimit < 23000 ;

select customerName, creditLimit from customers where creditLimit <> 23000 ;



