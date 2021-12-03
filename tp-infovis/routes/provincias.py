from fastapi import APIRouter
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.functions import func
from config.db import conn
from models.data import data
from models.generales import secciones
from schemas.generales import Agrupacion, Cargo, Seccion
from config.db import meta
from schemas.votos_totales import VotosTotales,AgrupacionVotosTotales
from typing import List

provincias = APIRouter()

@provincias.get("/provincia/{id_provincia}/cargos", response_model=list[Cargo], tags=["Provincias"])
def get_cargos_por_provincia(id_provincia: int):
    cargo_t=meta.tables['cargo']
    join_res = data.join(cargo_t, cargo_t.c.idcargo == data.c.idcargo)
    select_st=select([cargo_t.c.idcargo, cargo_t.c.cargo]).distinct().select_from(join_res).where(data.c.iddistrito == id_provincia)
    return conn.execute(select_st).fetchall()

@provincias.get("/provincia/{id_provincia}/votos", response_model=VotosTotales, tags=["Provincias"])
def get_votos_por_provincia_totales(id_provincia: int):
    select_st=select([func.sum(data.c.votos)]).select_from(data).where(data.c.iddistrito == id_provincia)
    res = conn.execute(select_st)
    return { "cant" : tuple(res)[0][0]}

@provincias.get("/provincia/{id_provincia}/agrupaciones", response_model=list[Agrupacion], tags=["Provincias"])
def get_agrupaciones_por_provincia(id_provincia: int):
    agp_t=meta.tables['agrupaciones']
    join_res = data.join(agp_t, agp_t.c.idagrupacionint == data.c.idagrupacionint)
    select_st=select([agp_t.c.idagrupacionint, agp_t.c.agrupacion]).distinct().select_from(join_res).where(data.c.iddistrito == id_provincia)
    return conn.execute(select_st).fetchall()

@provincias.get("/provincia/{id_provincia}/secciones", response_model=list[Seccion], tags=["Provincias"])
def get_secciones_por_provincia(id_provincia: int):
    return conn.execute(secciones.select().where(secciones.c.iddistrito == id_provincia)).fetchall()

@provincias.get("/provincia/{id_provincia}/cargo/{id_cargo}/agrupaciones/votos", response_model= list[AgrupacionVotosTotales], tags=["Provincias"])
def get_votos_por_cargo_por_provincia(id_provincia: int, id_cargo: int):
    agp_t=meta.tables['agrupaciones']
    join_res = data.join(agp_t, agp_t.c.idagrupacionint == data.c.idagrupacionint)
    select_st=select([agp_t.c.idagrupacionint, agp_t.c.agrupacion, func.sum(data.c.votos).label('sum')]).select_from(join_res).where(data.c.iddistrito == id_provincia,data.c.idcargo == id_cargo).group_by(agp_t.c.idagrupacionint, agp_t.c.agrupacion)
    return conn.execute(select_st).fetchall()

@provincias.get("/provincia/{id_provincia}/agrupacion/{id_agrupacion}/votos", response_model= list[AgrupacionVotosTotales], tags=["Provincias"])
def get_votos_por_cargo_por_provincia(id_provincia: int, id_agrupacion: int):
    agp_t=meta.tables['agrupaciones']
    join_res = data.join(agp_t, agp_t.c.idagrupacionint == data.c.idagrupacionint)
    select_st=select([agp_t.c.idagrupacionint, agp_t.c.agrupacion, func.sum(data.c.votos).label('sum')]).select_from(join_res).where(data.c.iddistrito == id_provincia,data.c.idagrupacionint == id_agrupacion).group_by(agp_t.c.idagrupacionint, agp_t.c.agrupacion)
    return conn.execute(select_st).fetchall()

@provincias.get("/provincia/{id_provincia}/votos/invalidos", response_model=VotosTotales, tags=["Provincias"])
def get_votos_invalidos_por_provincia_totales(id_provincia: int):
    select_st = select([func.sum(data.c.votos)]).select_from(data).where(data.c.iddistrito==id_provincia,data.c.tipovoto!='positivo')
    res = conn.execute(select_st)
    return { "cant" : tuple(res)[0][0]}
