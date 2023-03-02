from fastapi import APIRouter

from api.routers import  kombat_route

urls = APIRouter()

urls.include_router(
    kombat_route.router,
    prefix=""
)

