# დავალება 30

# შემსრულებელი: გიორგი ცუცქირიძე

# საჭირო ბიბლიოთეკების შემოტანა

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, \
     relationship
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, CHAR

# 1. sqlalchemy_ს გამოყენებით შექმენი sqlite_ის info.db ფაილი.

os.chdir("./homeworks/hw-34_2024-04-11")

Base = declarative_base()

engine = create_engine("sqlite:///info.db")

Base.metadata.create_all(bind=engine)

# 2. Info.db_ში შექმენი ერთმანეთზე დამოკიდებული სტუდენტებისა
#  და კურსების ცხრილი.

class Course(Base):
    __tablename__ = "courses"

    course_id = Column("id", Integer, primary_key=True)
    name = Column("name", String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Courses(name={self.name})"

  
class Student(Base):
    __tablename__ = "students"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    course_id = Column("course", String, ForeignKey("courses.id"))

    course =  relationship("Course")

    def __init__(self, name, course_id):
        self.name = name
        self.course = course_id
    
    def __repr__(self):
        return f"Students(name={self.name}, course={self.course_id})"

Base.metadata.create_all(bind=engine)


# 3. შეიტანე პირველ ცხრილში მინიმუმ 10 ჩანაწერი, 
# მეორეში მინიმუმ 5 კურსი.

Session = sessionmaker(bind=engine)
session = Session()

courses = ["Algebra", "Probability", "Statistics", "Calculus", \
           "Real Analysis", "Functional Analysis"]

courses_model = []
for c in courses:
    courses_model.append(Course(c))

session.add_all(courses_model)

# 4.	გამოიტანე ცხრილში არსებული ინფორმაცია __repr__ 
# მეთოდის დხმარებით.


#------------------------------------------------------------------#