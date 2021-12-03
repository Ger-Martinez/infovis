from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

cargos = Table("cargo", meta, Column("idcargo", Integer, primary_key=True), Column("cargo", String(255)))

agrupaciones = Table("agrupaciones", meta, Column("idagrupacionint", Integer, primary_key=True), Column("agrupacion", String(255)))

distritos = Table("distritos", meta, Column("iddistrito", Integer, primary_key=True), Column("distrito", String(255)))

secciones = Table("secciones", meta, Column("idsecc", Integer, primary_key=True), Column("iddistrito", Integer), Column("idseccion", Integer), Column("seccion", String(255)))