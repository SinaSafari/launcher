from typing import Dict


class AppInfoService:
    def __init__(self) -> None:
        pass

    def get_app_info(self) -> Dict[str, any]:
        return {
            "app_name": "launcher",
            "version": "0.0.1",
            "models": [
                {
                    "name": "diabetes",
                    "type_of_problem": "linear regression",
                    "routes": {
                        "train": "/diabetes/train",
                        "test": "/diabetes/test?data_diabetes=0.07786339",
                    },
                }
            ],
        }
