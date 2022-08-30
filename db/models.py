from db.session import Base
from sqlalchemy import Column,Integer, String, DateTime
from datetime import datetime


class User(Base):
    __tablename__='api'
    id=Column(Integer, primary_key=True,autoincrement=True)
    username=Column(String,unique=True)
    password=Column(String)
    nombre=Column(String)
    apellido=Column(String)
    direccion=Column(String)
    telefono=Column(String)
    #creacion= Column(DateTime,default=datetime.now,onupdate=datetime.now)
    