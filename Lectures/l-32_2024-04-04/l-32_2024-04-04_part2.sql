/* ლექცია 32: l32_2024-04-04 */

/* ლექცია 32-ზე დაწერილი კოდი */

/* ნაწილი 1 */

/* Relationships */

create schema school;

use school;

create table students 
(
	studentID int not null unique primary key auto_increment,
    firstName varchar(40) not null,
    class varchar(40),
    age int
);

insert into students 
(firstName, class, age)
values
("Nika", "first", 26),
("Mriami", "second", 22),
("George", "third", 32)
;

create table addresses
(
	addressID int not null unique primary key auto_increment, 
);