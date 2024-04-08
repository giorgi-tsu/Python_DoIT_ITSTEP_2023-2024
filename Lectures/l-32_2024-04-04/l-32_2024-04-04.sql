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


 
