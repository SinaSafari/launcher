from typing import Dict
from app.services.app_info_service import AppInfoService


class AppInfoController:
    def __init__(self) -> None:
        self.__app_info_service = AppInfoService()

    def app_info(self) -> Dict[str, str]:
        return self.__app_info_service.get_app_info()
