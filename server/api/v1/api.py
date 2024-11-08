from fastapi import APIRouter
from server.controller import cat_controller

api_router = APIRouter()
api_router.include_router(cat_controller.router, prefix="/cats", tags=["cats"]) 