#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI, HTTPException
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel
from fastapi import APIRouter


#Creamos un objeto a partir de la clase FastAPI
router = APIRouter()

class Country(BaseModel):
    code:str
    name:str
    code2:str

#LISTA DE PAISES CONTENIDOS EN LA REGION, INSTANCIADO CON BASEMODEL
#Country(code="", name="", code2=""),
contries_list = [
    Country(code="ATA", name="Antarctica", code2="AQ"),
    Country(code='SGS',name='South Georgia and the South Sandwich Islands',code2='GS'),
    Country(code='HMD',name='Heard Island and McDonald Islands',code2='HM'), 
    Country(code='ATF',name='French Southern territories',code2='TF'),
    Country(code='BVT',name='Bouvet Island',code2='BV'), 
]

#CREACION DE GET METHOD
@router.get("/antarctica/", status_code = 200)
async def region():
    return  (contries_list)

#GET METHOD WITH FILTER
@router.get("/antarctica/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/antarctica/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/antarctica/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/antarctica/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")