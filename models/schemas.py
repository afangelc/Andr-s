from datetime import datetime
from doctest import Example
from msilib.schema import Class
from pydantic import BaseModel, UUID1
import datetime as dt
from typing import Optional

class User(BaseModel):
    username:str
    password:str
    nombre:str
    apellido:str
    direccion:str
    telefono:str
    creacion:datetime=datetime.now()

class UserCreate(User):
    pass

class UserCreateResponse(UserCreate):
    id: UUID1
    created_at: dt.datetime
    updated_at: Optional[dt.datetime] = None

#class PersonaResponse(PersonaCrear):
    #ffdfpass

class ShowUser(BaseModel):
    username:str
    nombre:str
    class Config():
        orm_mode=True

class UpdateUser(BaseModel):
    username:str=None
    password:str=None
    nombre:str=None
    apellido:str=None
    direccion:str=None
    telefono:str=None


class UpdateResponse(UpdateUser):
    creacion:datetime=datetime.now()



