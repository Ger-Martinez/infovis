from fastapi import FastAPI
from routes.generales import generales
from routes.votos_totales import votos_totales
from routes.provincias import provincias
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Final Infovis API",
    description="Elecciones Generales 2021",
    openapi_tags=[{
        "name": "Datos Generales",
        "description": "Informacion sobre agrupaciones, distritos, secciones y cargos."
    },
    {
        "name": "Votos Totales",
        "description": "Cantidades totales para cada tipo de voto en todo el pais."
    }]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)

app.include_router(generales)

app.include_router(votos_totales)

app.include_router(provincias)