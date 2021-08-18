import os
from db.config import database


async def init_db(app_mode: str) -> None:
    """
    initialize database from created sql scripts in app startup.

    Parameters
    ----------
    app_mode
        this parameter determines whether sqlite should be chosen as
        database or postgres.
    """
    path_of_file = get_sqlite_script_path(app_mode)

    if not path_of_file:
        raise FileNotFoundError("sql files are not exists or the path is wrong")

    script = open(path_of_file, "r").read()

    for s in script.split("-- create"):
        await database.execute(s)
    print("💾 database initialized")


def get_sqlite_script_path(mode) -> str:
    """
    this function generates and returns connection string of database

    Parameters
    ----------
    mode
        determines which path should be returned. it should be `dev` or `prod`

    Returns
    -------
    path of sqlite database, or postgres connection string
    """
    sqlite_path = f"{os.getcwd()}/db/scripts/ddl/sqlite_db_schema.sql"
    pg_path = f"{os.getcwd()}/db/scripts/ddl/pg_db_schema.sql"

    if mode == "dev" and os.path.isfile(sqlite_path):
        return sqlite_path

    elif mode == "prod" and os.path.isfile(pg_path):
        return pg_path

    else:
        return ""
