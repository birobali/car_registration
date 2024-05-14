from typing import List

from pydantic import BaseModel, ConfigDict


class JarmuModelDTO(BaseModel):
    id: int
    uuid: str
    rendszam: str
    tulajdonos: str
    forgalmi_ervenyes: str
    adatok: List[str]
    model_config = ConfigDict(from_attributes=True)


class JarmuModelInputDTO(BaseModel):
    rendszam: str
    tulajdonos: str
    forgalmi_ervenyes: str
    adatok: List[str]
