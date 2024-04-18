import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, CHAR 
from random import choice


Base = declarative_base()


class Person(Base):
    __tablename__ = "persons"

    id = Column("id", Integer, primary_key=True)
    name =  Column("name", String)  # ქმნის ცხრილის სვეტს.
    age = Column("age", Integer)  # ქმნის ცხრილის სვეტს.

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"


os.chdir("./lectures/l-35_2024-04-15/dbs/sqlite")
print(os.getcwd())

database_path = "mydb.db"
if os.path.exists(database_path ):
    os.remove(database_path)

engine = create_engine("sqlite:///mydb.db") 

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

session = Session()

person = Person("Levani", 15)

session.add(person)

print(session.query(Person).all())