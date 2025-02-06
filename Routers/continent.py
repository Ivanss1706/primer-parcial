#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI, HTTPException
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel
from fastapi import APIRouter


#Creamos un objeto a partir de la clase FastAPI
router = APIRouter()

class Continent(BaseModel):
    cID: int
    name : str

continent_list = [
    Continent(cID = 1,name="North America"),
    Continent(cID = 2,name="South America"),
    Continent(cID = 3,name="Antartica"),
    Continent(cID = 4,name="Africa"),
    Continent(cID = 5,name="Asia"),
    Continent(cID = 6,name="Europa"),
    Continent(cID = 7,name="Oceania")
]

#CREACION DE GET METHOD
@router.get("/continent/", status_code = 200)
async def continent():
    return  (continent_list)

@router.get("/continent/{id}")
async def continent(id:int):
    continent = filter (lambda continent: continent.cID == id, continent_list)  #Función de orden superior
    try:
        return list(continent)[0]
    except:
        raise HTTPException(status_code = 404, detail="CONTINENTE NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/continent/", status_code = 201)
async def continent(continent:Continent):
    found = False
    
    for index, saved_user in enumerate(continent_list):
        if saved_user.cID == continent.cID:
            raise HTTPException(status_code = 409, detail="CONTINENTE YA REGISTRADO")
    else:
        continent_list.append(continent)
        return continent
#http://127.0.0.1:8000/continent/

#CREACION DE PUT METHOD
@router.put("/continent/", status_code = 200)
async def continent(continent:Continent):
    
    found = False
    
    for index, saved_user in enumerate(continent_list):
        if saved_user.cID == continent.cID:
            continent_list[index] = continent
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return continent

#DELETE METHOD
@router.delete("/continent/{id}", status_code = 200)
async def continent(id:int):
    
    found = False
    
    for index, saved_user in enumerate(continent_list):
        if saved_user.cID == id:
            del continent_list[index]
            found = True
            return "PAIS ELIMINADO"
        
    if not found:
        raise HTTPException(status_code = 401, detail="CONTINENTE NO ENCONTRADO")