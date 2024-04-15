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
        return f"name={self.name}, age={self.age}"
    
engine = create_engine("sqlite:///:memory:")

Base.metadata.create_all(bind=engine)

name = ["Giorgi", "Mariami", "Elene"]
age = [22, 23, 18]

Session = sessionmaker(bind=engine)
session = Session()


for i in range(15):
    person = Person(choice(name), choice(age))
    session.add(person)
    session.commit()

# მეორე ვარიანტი ნახე ვიდეოში

# all_persons = session.query(Person).all()
# print(all_persons)


# first_person = session.query(Person).all()[0]
# print(first_person)


# all_persons = session.query(Person).filter_by(name="Elene").all()
# print(all_persons)

# all_persons = session.query(Person).filter_by(age=22).all()
# print(all_persons)

# all_persons = session.query(Person).filter_by(name="Elene", age=22).all()
# print(all_persons)

# all_persons = session.query(Person).filter(Person.age > 22).all()
# print(all_persons)

# all_persons = session.query(Person).filter(Person.age > 22, Person.age < 30).all()
# print(all_persons)


# all_persons = session.query(Person).filter(Person.age > 22, Person.age < 30).first()
# session.delete(all_persons) # როცა წაშლას ვაკეთებთ უნდა გადავეთ ობიექტი.
# session.commit()

# print(all_persons)


# ele = session.query(Person).filter_by(name="Elene").first()
# ele.age = 55
# session.commit()

# all_persons = session.query(Person).where((Person.age >= 22) | (Person.name == "Elene")).all()
# print(all_persons)


all_persons = session.query(Person).where((Person.age >= 22) & (Person.name == "Elene")).all()
print(all_persons)