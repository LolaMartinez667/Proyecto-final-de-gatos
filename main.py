from fastapi import FastAPI
from server.api.v1.api import api_router
from server.database.database import engine, Base
from dotenv import load_dotenv
import os
import logging

load_dotenv()

Base.metadata.create_all(bind=engine)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="API de Gestión de Adopción y Cuidado de Gatos")

@app.on_event("startup")
async def startup_event():
    logger.info("Application startup")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutdown")

app.include_router(api_router) 