# ლექცია 35: L30_2024-04-15

# ლექცია ჩატარდა 2024 წლის 28 მარტს
# თემა: 1. UDP ჩათის აწყობა
#       2. მრავალგანშშტოებიანი და ასინქრონული ექო სერვერის
#         რეალიზაცია

#*******************************************************************#

# საჭირო ბიბლიოთეკების შემოტანა 
import os
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
    age = Column("age", Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self, name):
        return f"Person(name={self.name})"

os.chdir("./lectures/l-35_2024-04-15/dbs/sqlite")
print(os.getcwd())

# engine = create_engine("sqlite:///") # ამ შემთხვევაში ბაზის ფაილს 
# # არ შექმნის და ის მხოლოდ RAM-ში იარსებს.

engine = create_engine("sqlite:///mydb.db") # ამ შემთხვევაში ბაზის
# ფაილს შექმნის და ჩაწერს სამუშაო საქაღალდეში.

Base.metadata.create_all(bind=engine)   # ამ შემთხვევაში შექმნის ყველა 
# ცხრილს ყველა იმ კლასისგან, რომლის მშობელი კლასიც არის Base 
# კლასი. საგულისხმოა ის, რომ სწორედ ამ ბრძანების დროს შექმნის 
# ბაზასაც, რომელშიც ჩაწერს ყველა ამ ცხრილს. ამ ბრძანების გაშვებამდე 
# ბაზა არ იქმნება. ზედა ბრძანებით იქმნება მხოლოდ ძრავი, რომელიც
# განსაზღვრაავს ბაზის მახასიათებლებს და იმას, თუ სად უნდა იყოს ბაზის 
# ფაილები. იმისათვის, რომ შეიქმნას ბაზა და მისი ფაილები ამას 
# განსაზღვრავს სწორედ არგუმენტი bind, რომელიც ტოლია ძრავის. 
# სწორედ ამ ძრავმა იცის რა ტიპის ბაზა იქმნება და სად უდნა შევინახოთ 
# ეს ბაზა.


timestamp l35_2024-04-15_00_18_42













