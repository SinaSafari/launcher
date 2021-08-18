from dotenv import load_dotenv

load_dotenv("./.env.local")

import os
from fastapi import FastAPI
from db.config import database
from db.init_db import init_db


# routers
from app.api.v1.app_info import router as app_info_router
from app.api.v1.diabets import router as diabetes_router

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()
    await init_db(os.getenv("APP_MODE"))


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(app_info_router)
app.include_router(diabetes_router, prefix="/diabetes")
