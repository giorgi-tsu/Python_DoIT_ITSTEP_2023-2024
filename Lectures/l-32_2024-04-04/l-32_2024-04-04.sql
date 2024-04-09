/* ლექცია 32: l32_2024-04-04 */

/* ლექცია 32-ზე დაწერილი კოდი*/

use it_step;

select * from customers where customernumber = 112;  -- გამოგვაქვს სტრიქონი, სადაც customerNumber არის 112

delete from customers where customerNumber=112; -- ვშლით სტრიქონს, სადაც customerNumber არის 112. აქ არ წაშლის ვინაიდან სხვა ცხრილთან არსებობს კავშირი. ამას მერე ვისწავლით.

/* select-ის გამოყენების ვარიაციები */

select customerName, city from customers; -- ვნიშნავ მხოლოდ 2 სვეტს: customerName და city.

select customerName, city from customers limit 5; -- სტრიქონების რაოდენობის შეზღუდვა. გვაჩვენებს მხოლოდ პირველ 5 სტრიქონს.

select customerName, city from customers where city = "NYC"; -- მონიშნავს მხოლოდ ნიუ იორკის კლიენტებს.

select * from customers where city = "NYC"; -- მონიშნავს მხოლოდ ნიუ იორკის კლიენტებს. 

select * from customers where city = "NYC" and creditLimit > 90000; -- მონიშნავს მხოლოდ ნიუ იორკის კლიენტებს და 90000-ზე მეტი საკრედიტო ლიმიტის მქონეს.

select * from customers where city = "NYC" and creditLimit > 90000 and contactLastName="Young"; -- მონიშნავს მხოლოდ ნიუ იორკის კლიენტებს და 90000-ზე მეტი საკრედიტო ლიმიტის მქონეს და გვარი არის Young.

select * from customers where city = "NYC" or creditLimit > 90000; -- მონიშნავს მხოლოდ ნიუ იორკის კლიენტებს ან 90000-ზე მეტი საკრედიტო ლიმიტის მქონეს.

select * from customers where city = "NYC" or city = "Paris"; -- მონიშნავს ნიუ იორკის ან პარიზის კლიენტებს.

select * from customers where city in ("NYC", "Paris"); -- მონიშნავს ნიუ იორკის ან პარიზის კლიენტებს.

select * from customers where creditLimit between 90300 and 98800; -- გამოიტანს ყველა ჩანაწერს, სადაც საკრედიტო ლიმიტი მოცემულ შუალედშია.

select * from customers where 90300 <= creditLimit and creditLimit <= 98800; --    -- გამოიტანს ყველა ჩანაწერს, სადაც საკრედიტო ლიმიტი მოცემულ შუალედშია.

select * from customers where city in ("NYC", "Paris") order by customerName; -- მონიშნავს ნიუ იორკის ან პარიზის კლიენტებს და დაალაგებს ანბანურად.

select * from customers where city in ("NYC", "Paris") order by customerName, addressLine1; -- მონიშნავს ნიუ იორკის ან პარიზის კლიენტებს და დაალაგებს კლიენტების მიხედვით ანბანურად. თუ კლიენტების სახელები დამეთხვევ ერთმანეთს, მაშინ დაალაგებს მისამართების მიხედვით ასევე ანბანურად.

select * from customers where city in ("NYC", "Paris") order by customerName, customerNumber; -- მონიშნავს ნიუ იორკის ან პარიზის კლიენტებს და დაალაგებს კლიენტების მიხედვით ანბანურად. თუ კლიენტების ნომრეისს მიხედვით.

select * from customers where city in ("NYC", "Paris") order by customerNumber; -- მონიშნავს ნიუ იორკის ან პარიზის კლიენტებს და დაალაგებს კლიენტების ნომრის მიხედვით

select * from customers where city in ("NYC", "Paris") order by customerNumber limit 5; -- მონიშნავს ნიუ იორკის ან პარიზის კლიენტებს და დაალაგებს კლიენტების ნომრის მიხედვით

/* regex-ები SQL-ში*/

select * from customers where customerName like "%e"; -- მონიშნავს ყველა კლინეტს, სადაც customerName მთავრდება e-ზე.

select * from customers where customerName like "e%"; -- მონიშნავს ყველა კლინეტს, სადაც customerName იწყება e-ზე.

select * from custmers where customerName like "e%s"-- მონიშნავს ყველა კლინეტს, სადაც customerName იწყება e-ზე და მთავრდება ს-ზე.



