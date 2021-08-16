from fastapi import FastAPI

# routers
from app.api.v1.app_info import router as app_info_router
from app.api.v1.diabets import router as diabetes_router

app = FastAPI()

app.include_router(app_info_router)
app.include_router(diabetes_router, prefix="/diabetes")
