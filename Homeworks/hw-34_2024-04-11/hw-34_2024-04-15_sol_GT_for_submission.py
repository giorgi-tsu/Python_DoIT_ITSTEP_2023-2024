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

os.chdir("./homeworks/hw-34_2024-04-11/dbs/sqlite")

print(os.getcwd())

Base = declarative_base()

database_path = "info.db" 

if os.path.exists(database_path):
    os.remove(database_path)

engine = create_engine("sqlite:///info.db")

Base.metadata.create_all(bind=engine)

# 2. Info.db_ში შექმენი ერთმანეთზე დამოკიდებული სტუდენტებისა
#  და კურსების ცხრილი.

class Course(Base):
    __tablename__ = "courses"

    course_id = Column("id", Integer, primary_key=True, \
                       autoincrement=True)
    name = Column("name", String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Courses(id = {self.course_id}, name={self.name})"

  
class Student(Base):
    __tablename__ = "students"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    course_id = Column("course", String, ForeignKey("courses.id"))

    course =  relationship("Course")

    def __init__(self, name, course_id):
        self.name = name
        self.course_id = course_id
    
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

# print(courses_model)

session.add_all(courses_model)
session.commit()

student_names = ["Ilia", "Ako", "Gabo", "Gio", "Papuna", "Rezo",\
                 "Semi", "Bacho", "Buta", "Geno", "Joni", "Ana"]
student_course_id = [1, 2, 3, 5, 6]

students_model = []

for sn in student_names:
    for sci in student_course_id:
        students_model.append(Student(sn, sci))

# print(students_model)

session.add_all(students_model)
session.commit()

# 4. გამოიტანე ცხრილში არსებული ინფორმაცია __repr__ 
# მეთოდის დხმარებით.

all_courses = session.query(Course).all()
print(all_courses)


all_students = session.query(Student).all()
print(all_students)


#------------------------------------------------------------------#