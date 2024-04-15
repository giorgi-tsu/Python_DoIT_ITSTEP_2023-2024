from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base

from sqlalchemy import ForeignKey, Column, Integer, String, CHAR

from random import choice

Base = declarative_base()

class Person(Base):
    __tablename__ = "Persons"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    age = Column("age", Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name={self.name})"
    
engine = create_engine("sqlite:///")

Base.metadata.create_all(bind=engine)

name = ["Giorgi", "Mariami", "Elene"]
age = [22, 23, 18]


