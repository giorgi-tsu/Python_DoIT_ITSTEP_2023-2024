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
	productID int auto_increment not null primary key,
    name varchar(50) not null,
    price int not null,
    categoryID int not null,
    foreign key (categoryID) references categories (categoryID)
);

select * from products;

insert into categories
(name)
value
("Electronics"),
("Food");

select * from categories;

insert into products
(name, price, categoryID)
values
("Apple", 2, 2),
("Milk", 1, 2),
("TV", 400, 1),
("Laptop", 3800, 1);

select * from products;

select * from categories;

-- timestamp: 01-30-32

/* რამდენიმე ცხრილის ერთდროულად გამოტანა */

select * from products cross join categories;

