from pydantic import BaseModel

class Cargo(BaseModel):
    idcargo: int
    cargo: str


class Agrupacion(BaseModel):
    idagrupacionint: int
    agrupacion: str


class Distrito(BaseModel):
    iddistrito: int
    distrito: str


class Seccion(BaseModel):
    idsecc: int
    iddistrito: int
    idseccion: int
    seccion: str