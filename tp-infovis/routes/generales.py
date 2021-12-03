from fastapi import APIRouter
from fastapi.params import Header
from schemas.generales import Cargo, Agrupacion, Distrito, Seccion
from models.generales import cargos, distritos, agrupaciones, secciones
from config.db import conn

generales = APIRouter()

@generales.get("/cargos", response_model=list[Cargo], tags=["Datos Generales"])
def get_cargos():
    return conn.execute(cargos.select()).fetchall()

@generales.get("/agrupaciones", response_model=list[Agrupacion], tags=["Datos Generales"])
def get_agrupaciones():
    return conn.execute(agrupaciones.select()).fetchall()

@generales.get("/provincias", response_model=list[Distrito], tags=["Datos Generales"])
def get_provincias():
    return conn.execute(distritos.select()).fetchall()

@generales.get("/secciones", response_model=list[Seccion], tags=["Datos Generales"])
def get_votos_totales():
    return conn.execute(secciones.select()).fetchall()