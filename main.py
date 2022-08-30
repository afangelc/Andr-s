from fastapi import FastAPI
from routes.routes import router
from db.session import Base, engine

# def crear_tabla(): #Crea las tablas en la base de datos
#     Base.metadata.create_all(bind=engine)

app=FastAPI()
app.include_router(router)


