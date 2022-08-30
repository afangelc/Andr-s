from multiprocessing import synchronize
from models import schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends,status
from db import models
from db.session import get_db


def crear_usuario(user:models.User, db:Session=Depends(get_db)):
    usuario=user.dict()
    nuevo_usuario=models.User(
        username=usuario["username"],
        password=usuario["password"],
        nombre=usuario["nombre"],
        apellido=usuario["apellido"],
        direccion=usuario["direccion"],
        telefono=usuario["telefono"],
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

def obtener_datos(user_id:int, db:Session=Depends(get_db)):
    usuario=db.query(models.User).filter(models.User.id==user_id).first()
    
    if not usuario:
        return {"respuesta":"usuario no encontrado!!"}
    
    return usuario

def eliminar_registro(user_id:int, db:Session=Depends(get_db)):
    usuario=db.query(models.User).filter(models.User.id==user_id)
    if not usuario.first():
        return {"respuesta":"usuario no encontrado"}
    usuario.delete(synchronize_session=False)
    db.commit()
    return{"respuesta":"usuario eliminado correctamente"}

def modificar_registro(user_id, update_user, db:Session):
    usuario=db.query(models.User).filter(models.User.id==user_id)    
    if not usuario.first():
        return {"respuesta":"usuario no encontrado"}
    usuario.update(update_user.dict(exclude_unset=True))
    db.commit()
    return{"respuesta":"usuario modificado correctamente"}

def funcion(id:int):
    return "hola"




    


