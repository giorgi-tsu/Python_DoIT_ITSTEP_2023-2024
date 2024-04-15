/*  დავალება 33 */

/*
1. IT_Step_ის მონაცემთა ბაზაში, პროდუქტების ცხრილში, აგრეგაციის ფუნქციის დახმარებით გამოთვალე პროდუქტის საშულო ფასი.
*/

use it_step;

select productName, avg(buyPrice) from products group by productName; -- პროდუქტის საშუალო ფასი თითოეული პროდუქტისთვის.

select avg(buyPrice) as average_price from products; -- ყველა პროდუქტის საშუალო ფასი.


/*
2.	მონიშნე ყველა ის პროდუქტი, რომლის ფასიც საშუალოზე მაღალია.
*/

select productName, buyPrice from products where buyPrice > (select avg(buyPrice) from products) order by buyPrice; -- საშუალო ფასია: '54.395182' და
-- მართლაც ვხედავთ რომ გამაოქვს ყველა პროდუტი, სადაც ფასი საშუალოზე მეტია.



