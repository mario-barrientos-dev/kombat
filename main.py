from fastapi import FastAPI
from api.routers import  kombat_route


app = FastAPI(
    title="Talana Kombat",
    description="Esta es una aplicación de simulación de combate",
    version="1.0.0",
)


app.include_router(kombat_route.router) 