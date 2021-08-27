import os

APP_BASE_PATH = f"{os.getcwd()}/app"

app_paths = {
    "models": f"{APP_BASE_PATH}/models",
    "repos": f"{APP_BASE_PATH}/repositories",
    "services": f"{APP_BASE_PATH}/services",
    "controllers": f"{APP_BASE_PATH}/controllers",
    "api": f"{APP_BASE_PATH}/api/v1",
}

msg_colors = {
    "error": "red",
    "warning": "yellow",
    "success": "green",
    "info": "grey",
}
