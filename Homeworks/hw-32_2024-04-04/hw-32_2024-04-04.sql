/*  დავალება 32 */

/*
1. IT_Step_ის მონაცემთა ბაზაში cross join_ის დახმარებით გამოიტანე ორი ცხრილიდან ამოღებული სასურველი ინფორმაცია.
*/

use it_step;

select count(*) from customers;
select count(*) from products;
select count(*) from customers cross join products;
select customerName, productName from customers cross join products;


/*
2. შექმენი ორი ცხრილი. დააკავშირე ცხრილები foreign key_ს  გამოყენებით. დაამატე ცხრილებში ინფორმაცია.
*/

create schema hw_32;

use hw_32;

create table table_1 (
	city varchar(45) not null unique primary key,
	state varchar(45) not null,
    country varchar(45) not null
);


create table table_2 (
	personID int not null auto_increment,
	firstName varchar(45) not null,
    lastName varchar(45) not null,
    city  varchar(45) not null,
    primary key (personID),
    foreign key (city) references table_1(city)
);

insert into table_1 (city, state, country)
values 
("Tbilisi", "Tbilisi", "Georgia"),
("Kutaisi", "Imereti", "Georgia"),
("NYC", "NY", "USA");

select * from table_1;

insert into table_2 
(firstName, lastName, city)
values
("Saba", "Barbakadze", "Kutaisi"),
("Lena", "Bukuri", "Kutaisi"),
("Jack", "Smith", "NYC");

select * from table_2;