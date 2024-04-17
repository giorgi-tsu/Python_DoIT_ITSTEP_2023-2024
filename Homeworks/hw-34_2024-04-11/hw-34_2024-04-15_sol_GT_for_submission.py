

# 2.	Info.db_ში შექმენი ერთმანეთზე დამოკიდებული სტუდენტებისა და კურსების ცხრილი.
# 3.	შეიტანე პირველ ცხრილში მინიმუმ 10 ჩანაწერი, მეორეში _ მინიმუმ 5 კურსი.
# 4.	გამოიტანე ცხრილში არსებული ინფორმაცია __repr__ მეთოდის დხმარებით.


# დავალება 30

# შემსრულებელი: გიორგი ცუცქირიძე

# საჭირო ბიბლიოთეკების შემოტანა


# 1. sqlalchemy_ს გამოყენებით შექმენი sqlite_ის info.db ფაილი.


# საჭირო ბიბლიოთეკების შემოტანა

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker 
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, CHAR

#------------------------------------------------------------------#