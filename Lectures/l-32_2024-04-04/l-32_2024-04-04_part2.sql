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

select * from students;

insert into students 
(firstName, class, age)
values
("Nika", "first", 26),
("Mriami", "second", 22),
("George", "third", 32);

select * from students;

create table addresses
(
	addressID int not null unique primary key auto_increment,
    address varchar(100) not null,
    studentID int not null unique,
    foreign key (studentID) references students(studentID)
);
 
select * from addresses;

insert into addresses 
(address, studentID)
values
("Tbilisi", 1),
("Kutaisi", 3),
("Batumi", 2);

select * from addresses;

delete from students where studentID = 1; -- ამ შემთხვევაში არ წაშლის, ვინაიდან students(studentID) ველი არის addresses(studentID) ველის მშობელი (parent).
-- ეს მოხდა ვინაიდან addresses ცხრილში, ჩვენ მივუთითეთ, რომ ამ ცხრილის studentID არის foreign key და მისი references არის studentID students ცხრილიდან
-- (foreign key (studentID) references students(studentID)). Error Code: 1451. Cannot delete or update a parent row: a foreign key constraint fails
-- (`school`.`addresses`, CONSTRAINT `addresses_ibfk_1` FOREIGN KEY (`studentID`) REFERENCES `students` (`studentID`))


