from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base

from sqlalchemy import ForeignKey, Column, Integer, String, CHAR

Base = declarative_base()

class Person(Base):
    