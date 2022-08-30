from ntpath import join
from struct import pack
from fastapi.testclient import TestClient
import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.join(os.path.dirname(__file__),'../'))
from main import app

db_path = os.path.join(os.path.dirname(__file__),'test.db')
db_uri = "sqlite:///{}".format(db_path)

cliente=TestClient(app)

def test_crear_usuario():

    usuario = {
        "username": "jk",
        "password": "vn",
        "nombre": "g",
        "apellido": "v",
        "direccion": "x",
        "telefono": "d",
        "creacion": "2022-08-25T17:00:24.554000"
    }

    response=cliente.post('/user/', json=usuario)
    assert response.status_code ==201
    pass

def test_obtener_usuario():
    response = cliente.get('/user/90')
    assert response.json()["username"] == "jk"

def test_eliminar_usuario():
    response = cliente.delete('/user/90')
    assert response.json()["respuesta"] == "usuario eliminado correctamente!"
    response_user = cliente.get('/user/90')
    assert response_user.json()["respuesta"] == "usuario no encontrado con el id 1"
    print(response.json())




    
