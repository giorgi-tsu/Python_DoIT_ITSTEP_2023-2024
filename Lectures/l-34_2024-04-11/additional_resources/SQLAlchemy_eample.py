from sqlalchemy import create_engine, ForeignKey,\
Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = "people"

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    firstname = Column("laststname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    