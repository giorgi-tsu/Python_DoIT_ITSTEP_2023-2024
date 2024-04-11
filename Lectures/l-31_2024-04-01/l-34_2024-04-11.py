from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Boolean, CHAR, ForeignKey
from sqlalchemy import  create_engine

Base = declarative_base()

class Person(Base):
    __tablename__ = "persons"
    person_id = Column("person_id", Integer, primary_key=True)
    firstname = Column("firstname", String)
    firstname = Column("lastname", String)
    gender = Column("gender", CHAR)

    def __init__(self, person_id, firstname, lastname, gender, age):
        self.person_id = person_id        
        self.firstname = firstname        
        self.lastname = lastname        
        self.gender = gender        
        self.age = age
    
    def __repr__(self):
        return f"{self.person_id}|{self.firstname}|{self.lastname}|{self.gender}|{self.age}"

# engine = create_engine("sqlite:///mydb.db")
engine = create_engine("sqlite:///") # ramSi sheiqmneba
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person1 = Person(12345, "Nika", "Tsitskishvili", "M", 28)
person2 = Person(34521, "Mariam", "Bliadze", "F", 22)
person3 = Person(87609, "Davit", "Loladze", "M", 31)

session.add(person1)
session.add(person2)
session.add(person3)

session.commit()

result = session.query(Person).all()
print(result)


class Thing(Base):
    __tablename__ = "things"

    id = Column("id", Integer, primary_key=True,autoincrement=True)
    description = Column("description", String)
    owner = Column(Integer, ForeignKey("persons.person.id"), unique=True)

    def __init__(self, description, owner)