from fastapi import APIRouter
from app.controllers.app_info_controller import AppInfoController

router = APIRouter()


@router.get("/")
def get_app_info():
    app_info_controller = AppInfoController()
    return app_info_controller.app_info()
