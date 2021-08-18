from dotenv import load_dotenv

load_dotenv("./.env.local")

import os
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
import graphene

from db.config import database
from db.init_db import init_db
from app.graphql.queries import Query


# routers
from app.api.v1.app_info import router as app_info_router
from app.api.v1.diabets import router as diabetes_router

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()
    # todo: make it runs once. in sql code or in python
    await init_db(os.getenv("APP_MODE"))


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# restapi routes
app.include_router(app_info_router, prefix="/api/v1")
app.include_router(diabetes_router, prefix="/api/v1")

# graphql app
app.add_route("/gql", GraphQLApp(schema=graphene.Schema(query=Query)))
