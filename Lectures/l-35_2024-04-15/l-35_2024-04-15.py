# ლექცია 35: L30_2024-04-15

# ლექცია ჩატარდა 2024 წლის 28 მარტს
# თემა: 1. UDP ჩათის აწყობა
#       2. მრავალგანშშტოებიანი და ასინქრონული ექო სერვერის
#         რეალიზაცია

#*******************************************************************#

# საჭირო ბიბლიოთეკების შემოტანა 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, CHAR 


#*******************************************************************#

# ლექციის კოდი

Base = declarative_base()  # ამ ბრძანებით ვქმნით Base კლასს, 
# რომელსაც შემდეგ ვიყენებთ ცხრილების შესაქმნელად. ამისათვის კი
# ცხრილის კლასში მშობელ კლასად გადავემთ Base კლასს.

# ქვემოთ მოცემული კლასი ქმნის ცხრილის სტრუქტურას.
# მიღებულია, რომ კლასს და ამ კლასით შემქნილ ცხრილს ჰქონდეთ ერთი
# და იგივე სახელები, ოღონდ კლასის სახელი იყოს მხოლობითში, ხოლო
# ცხრილის სახელი იყოს მრავლობითში.
class Person(Base):
    __tablename__ = "persons" # ცხრილის სახელი

    # ვქმნით კლასის ატრიბუტებს, რომელიც წარმოადგენს იმ ცხრილის
    # სვეტებს(ატრიბუტებს), რომელიც შეიქმნება ამ კლასისგან.

    id = Column("id", Integer, primary_key=True) # ეს ქმნის ცხრილის
    # სვეტებს, ისე როგორც sql-ში იყო. ვუთითებთ სვეტის(ატრიბუტის)
    # სახელს, სვეტის ტიპს და არის თუ არა ის ცხრილის ძირითადი
    # გასაღები.

    name =  Column("name", String)  # ქმნის ცხრილის სვეტს.


















