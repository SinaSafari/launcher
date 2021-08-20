import os
from db.config import database
from db.init_db import init_db


async def on_app_startup():
    await database.connect()
    app_mode = os.getenv("APP_MODE")

    if app_mode == "dev":
        db_exists = await check_for_sqlite()

        if not db_exists:
            await init_db(app_mode)
        else:
            print("💾 `mydb.db` is exists. initialization process ignored.")


async def on_app_shut_down():
    await database.disconnect()


async def check_for_sqlite():
    sqlite_path = f"{os.getcwd()}/mydb.db"
    return os.path.isfile(sqlite_path)
