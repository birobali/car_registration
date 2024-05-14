import uuid
from typing import List

from pydantic import BaseModel


class JarmuModel(BaseModel):
    uuid: uuid.UUID
    rendszam: str
    tulajdonos: str
    forgalmi_ervenyes: str
    adatok: List[str]
