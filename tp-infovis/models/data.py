from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from config.db import meta, engine

data = Table("data", meta, 
    Column("codigo", Integer), 
    Column("establecimiento", String(255)),
    Column("fecha", DateTime),
    Column("idcargo", Integer, ForeignKey("cargo.idcargo")),
    Column("idcircuito", Integer),
    Column("iddistrito", Integer, ForeignKey("distritos.idditrito")),
    Column("idsecc", Integer, ForeignKey("secciones.idsecc")),
    Column("mesa", String(255)),
    Column("idagrupacionint", Integer, ForeignKey("agrupaciones.idagrupacionint")),
    Column("tipovoto", String(255)),
    Column("votos", Integer))