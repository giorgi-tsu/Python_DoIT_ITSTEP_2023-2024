/* ლექცია 32: l32_2024-04-04 */

/* ლექცია 32-ზე დაწერილი კოდი */

/* ნაწილი 4 */

/* Relationships */

/* Many to many relationship (m-m) */

-- timestamp: 01-33-20

create database manytomany;

use manytomany;

create table products
(
	productID int auto_increment not null primary key,
    name varchar(50) not null,
    price int not null,
    categoryID int not null
);

insert into products
(name, price, categoryID)
values
("Apple", 2, 2),
("Milk", 1, 2),
("TV", 400, 1),
("Laptop", 3800, 1);



-- აქ უკვე ძაან ბოდიალი იყო და იუზლეს იყო ამ ვიდეოს ხელალა ყურება.