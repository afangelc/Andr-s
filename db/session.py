from click import echo
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from core.config import settings


#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Aprend1z.22@localhost/postgres"
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine=create_engine(SQLALCHEMY_DATABASE_URL,echo=True) #Interactúa con las tablas de datos
SessionLocal=sessionmaker(bind=engine)
Base=declarative_base() #declara los modelos


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close


