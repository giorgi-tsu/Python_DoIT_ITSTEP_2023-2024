/* ლექცია 32: l32_2024-04-04 */

/* ლექცია 32-ზე დაწერილი კოდი */

/* ნაწილი 3 */

/* Relationships */

/* One to many relationship (1-1) */

create schema onetomany;

use onetomany;

create table categories
(
	categoryID int auto_increment not null primary key,
    name varchar(50) not null
);

select * from categories;

create table products
(
	categoryID int auto_increment not null primary key,
    name varchar(50) not null,
    price int not null,
    categoryID int not null,
    foreign key (categoryID) references categories (categoryID)
);

insert into categories
(name)
values
()