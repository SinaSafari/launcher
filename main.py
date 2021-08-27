from dotenv import load_dotenv

load_dotenv("./.env.local")

import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.graphql import GraphQLApp
import graphene
from fastapi_jwt_auth import AuthJWT

from app.graphql.queries import Query
from lib.app.events import on_app_startup, on_app_shut_down
from config.auth import AuthSettings

# routers
from app.api.v1.app_info import router as app_info_router
from app.api.v1.diabets import router as diabetes_router

app = FastAPI()


@app.on_event("startup")
async def startup():
    await on_app_startup()


@app.on_event("shutdown")
async def shutdown():
    await on_app_shut_down()


@AuthJWT.load_config
def get_config():
    return AuthSettings()


# static files route
app.mount("/static", StaticFiles(directory="public"), name="static")

# restapi routes
app.include_router(app_info_router, prefix="/api/v1")
app.include_router(diabetes_router, prefix="/api/v1")

# graphql app
app.add_route("/gql", GraphQLApp(schema=graphene.Schema(query=Query)))
