/*  დავალება 31 */

/*
1. IT_Step_ის მონაცემთა ბაზაში, customers_ცხრილში შეცვალე ყველა იმ მომხმარებლის contactLastName, ვისაც contactLastName აქვს “Lee”.
*/

use it_step;

select * from customers order by contactLastName;

select contactLastName, contactFirstName from customers order by contactLastName;

/* მაინტერესებს რამდენი "Lee" არის customers ცხრილში*/

select count(contactLastName) from customers as contactLastNameNumber where contactlastName = "Lee" order by contactLastName;

/* customers ცხრილში არის 1 "Lee"  */
 
update customers set contactLastName = "New_Lee" where contactLastName = "Lee";

/* 
2.	შექმენი ახალი Schema და მასში ორი ცხრილი. დაამატე ცხრილებში მინიმუმ სამ-სამი ინფორმაცია insert_ის გამოყენებით. წაშალე ცხრილი. წაშალე სქემა. 
*/

create schema hw_31;

use hw_31;

create table table_1 (
	personID int not null auto_increment,
	firstName varchar(45) not null,
    lastName varchar(45) not null,
    city  varchar(45),
    primary key (personID)
);

create table table_2 (
	personID int not null auto_increment,
	state varchar(45) not null,
    country varchar(45) not null,
    primary key (personID)
);

insert into table_1 (firstName, lastName, city)
values 
("Nika", "Kvekveskiri", "Gali"),
("Budu", "Zivzivadze", "Kutaisi"),
("Khvicha", "Kvaratskheia", "Tsalenjikha");

select * from table_1;

insert into table_2 
(state, country)
values
("Imereti", "Georgia"),
("Imereti", "Georgia"),
("Samegrelo", "Georgia");

select * from table_2;

drop table table_1;

drop table table_2;

drop schema hw_31;

