from typing import List

from fastapi import APIRouter, Response, status
from fastapi.param_functions import Depends

from car_registration.db.dao.jarmu_dao import JarmuDAO
from car_registration.db.models.jarmu_model import JarmuModel
from car_registration.web.api.jarmu.schema import JarmuModelInputDTO

router = APIRouter(redirect_slashes=False)


@router.get("/jarmuvek", response_model=int)
async def get_jarmu_count(
    jarmu_dao: JarmuDAO = Depends(),
) -> int:
    return await jarmu_dao.get_jarmu_count()


@router.get("/jarmuvek/{uuid}", response_model=JarmuModel)
async def get_jarmu_model(
    uuid: str,
    jarmu_dao: JarmuDAO = Depends(),
) -> JarmuModel:
    return await jarmu_dao.get_jarmu(uuid)


@router.post("/jarmuvek", status_code=status.HTTP_201_CREATED)
async def create_jarmu_model(
    new_jarmu_object: JarmuModelInputDTO,
    response: Response,
    jarmu_dao: JarmuDAO = Depends(),
) -> None:
    import uuid

    uuid = uuid.uuid4()
    response.headers["Location"] = f"/jarmuvek/{str(uuid)}"
    await jarmu_dao.create_jarmu_model(
        uuid=uuid,
        rendszam=new_jarmu_object.rendszam,
        tulajdonos=new_jarmu_object.tulajdonos,
        forgalmi_ervenyes=new_jarmu_object.forgalmi_ervenyes,
        adatok=new_jarmu_object.adatok,
    )


@router.get("/kereses", response_model=List[JarmuModel])
async def get_jarmu_by_filter(
    q: str,
    jarmu_dao: JarmuDAO = Depends(),
) -> List[JarmuModel]:
    return await jarmu_dao.get_jarmu_by_filter(q)
