create schema test2;

use test2;
create table persons (
	personID int not null auto_increment,
    lastname varchar(45) not null,
    firstname varchar(45) not null,
    city  varchar(45),
    primary key (personID)
    );
persons