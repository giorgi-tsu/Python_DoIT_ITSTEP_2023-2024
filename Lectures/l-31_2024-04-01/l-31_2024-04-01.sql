create schema test2;

use test2;
create table persons (
	personID int not null auto_increment,
    lastname varchar(45) not null,
    firstname varchar(45) not null,
    city  varchar(45),
    primary key (personID)
    );
    

select * from test2.persons;

insert into	persons (lastname, firstname, city)
values 
("Khoshtaria", "Davit", "Zugdidi"),
("Mikhelidze", "Mariam", "Kutaisi");

delete from persons where firstname="Nika";

update persons 
set city = "poti", lastname = "Tutashkhia"
where personID=2