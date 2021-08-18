import os
from db.config import database


async def init_db(app_mode: str) -> None:
    """
    initialize database from created sql scripts in app startup.
    """
    path_of_file = get_sqlite_script_path(app_mode)

    if not path_of_file:
        raise FileNotFoundError("sql files are not exists or the path is wrong")

    file = open(path_of_file, "r")
    script = file.read()
    await database.execute(script)
    print("💾 database initialized")


def get_sqlite_script_path(mode) -> str:
    sqlite_path = f"{os.getcwd()}/db/scripts/sqlite_db_schema.sql"
    pg_path = f"{os.getcwd()}/db/scripts/pg_db_schema.sql"

    if mode == "dev" and os.path.isfile(sqlite_path):
        return sqlite_path

    elif mode == "prod" and os.path.isfile(pg_path):
        return pg_path

    else:
        return ""
