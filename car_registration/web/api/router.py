from fastapi.routing import APIRouter

from car_registration.web.api import echo, jarmu, monitoring

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(jarmu.router, tags=["jarmuvek"])
