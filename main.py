import logging
from fastapi import FastAPI
from server.api.v1.api import api_router
from server.database.database import engine, Base
from dotenv import load_dotenv
import os

load_dotenv()

Base.metadata.create_all(bind=engine)

logging.basicConfig(level=logging.DEBUG)

app = FastAPI(title="API de Gestión de Adopción y Cuidado de Gatos")

app.include_router(api_router) 