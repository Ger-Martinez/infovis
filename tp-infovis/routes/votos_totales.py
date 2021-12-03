from fastapi import APIRouter
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.functions import func
from config.db import conn
from models.data import data
from schemas.votos_totales import VotosTotales

votos_totales = APIRouter()


@votos_totales.get("/votos", response_model=VotosTotales, tags=["Votos Totales"])
def get_votos_totales():
    res = conn.execute(select([func.sum(data.c.votos)]).select_from(data))
    return { "cant" : tuple(res)[0][0]}

@votos_totales.get("/votos/blancos", response_model=VotosTotales, tags=["Votos Totales"])
def get_votos_blancos_totales():
    res = conn.execute(select([func.sum(data.c.votos)]).select_from(data).where(data.c.tipovoto=='blancos'))
    return { "cant" : tuple(res)[0][0]}

@votos_totales.get("/votos/nulos", response_model=VotosTotales, tags=["Votos Totales"])
def get_votos_nulos_totales():
    res = conn.execute(select([func.sum(data.c.votos)]).select_from(data).where(data.c.tipovoto=='nulos'))
    return { "cant" : tuple(res)[0][0]}

@votos_totales.get("/votos/recurridos", response_model=VotosTotales, tags=["Votos Totales"])
def get_votos_recurridos_totales():
    res = conn.execute(select([func.sum(data.c.votos)]).select_from(data).where(data.c.tipovoto=='recurridos'))
    return { "cant" : tuple(res)[0][0]}

@votos_totales.get("/votos/comando", response_model=VotosTotales, tags=["Votos Totales"])
def get_votos_comando_totales():
    res = conn.execute(select([func.sum(data.c.votos)]).select_from(data).where(data.c.tipovoto=='comando'))
    return { "cant" : tuple(res)[0][0]}

@votos_totales.get("/votos/impugnados", response_model=VotosTotales, tags=["Votos Totales"])
def get_votos_impugnados_totales():
    res = conn.execute(select([func.sum(data.c.votos)]).select_from(data).where(data.c.tipovoto=='impugnados'))
    return { "cant" : tuple(res)[0][0]}

#https://www.pythonsheets.com/notes/python-sqlalchemy.html