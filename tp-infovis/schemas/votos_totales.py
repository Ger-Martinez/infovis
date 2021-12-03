from pydantic import BaseModel
from typing import Optional

class VotosTotales(BaseModel):
    cant: int

class AgrupacionVotosTotales(BaseModel):
    idagrupacionint: int
    agrupacion: str
    sum: Optional [int]