from fastapi import APIRouter, Depends,status
from models.schemas import UpdateUser, User
from sqlalchemy.orm import Session
from db.session import get_db
from db import models
from crud import services as crud
from models.schemas import ShowUser
from models import schemas



router=APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.get('/{user_id}', response_model=ShowUser)
def obtener(user_id:int, db:Session=Depends(get_db)):
    usuario=crud.obtener_datos(user_id,db)
    #data=db.query(models.User).all() # 
    return usuario
    


@router.post('/',status_code=status.HTTP_201_CREATED)
def crear(user:User, db:Session=Depends(get_db)):
    r=crud.crear_usuario(user,db)
    return {"respuesta":"el usuario se creó satisfactoriamente"}
    

@router.delete('/{user_id}')
def borrar(user_id:int, db:Session=Depends(get_db)):
    res=crud.eliminar_registro(user_id,db)
    return res

@router.patch('/{user_id}')
def modificar(user_id:int, update_user:UpdateUser,db:Session=Depends(get_db)):
    res = crud.modificar_registro(user_id,update_user, db)
    return res




    

