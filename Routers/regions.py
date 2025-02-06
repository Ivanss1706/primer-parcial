#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI, HTTPException
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel
from fastapi import APIRouter


#Creamos un objeto a partir de la clase FastAPI
router = APIRouter()

class Region(BaseModel):
    rID: int
    name : str
    
regions_list = [
    Region(rID = 1,name="Antartica"),
    Region(rID = 2,name="Caribbean"),
    Region(rID = 3,name="Australia and New Zealand"),
    Region(rID = 4,name="Baltic Countries"),
    Region(rID = 5,name="British Islands"),
    Region(rID = 6,name="Central Africa"),
    Region(rID = 7,name="Central America")
]

#CREACION DE GET METHOD
@router.get("/region/", status_code = 200)
async def region():
    return  (regions_list)

@router.get("/region/{id}")
async def region(id:int):
    id.upper()
    region = filter (lambda region: region.rID == id, regions_list)  #Función de orden superior
    try:
        return list(region)[0]
    except:
        raise HTTPException(status_code = 404, detail="REGION NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/region/", status_code = 201)
async def continent(region:Region):
    found = False
    
    for index, saved_user in enumerate(regions_list):
        if saved_user.rID == region.rID:
            raise HTTPException(status_code = 409, detail="REGION YA REGISTRADA")
    else:
        regions_list.append(region)
        return continent
#http://127.0.0.1:8000/region/

#CREACION DE PUT METHOD
@router.put("/region/", status_code = 200)
async def continent(region:Region):
    
    found = False
    
    for index, saved_user in enumerate(regions_list):
        if saved_user.rID == region.rID:
            regions_list[index] = region
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return region

#DELETE METHOD
@router.delete("/region/{id}", status_code = 200)
async def continent(id:int):
    
    found = False
    
    for index, saved_user in enumerate(regions_list):
        if saved_user.rID == id:
            del regions_list[index]
            found = True
            return "REGION ELIMINADA"
        
    if not found:
        raise HTTPException(status_code = 401, detail="REGION NO ENCONTRADA")