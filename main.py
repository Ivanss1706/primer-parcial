#IMPORTACION DE FASTAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
#IMPORTAMCION DESDE LA CARPETA ROUTER
from Routers import country, continent, regions, antartica

#CREACION DEL OBJETO APP
app = FastAPI()
app.include_router(country.router)
app.include_router(continent.router)
app.include_router(regions.router)
app.include_router(antartica.router)

@app.get("/")
async def imprimir():
    return "Hola todos"


