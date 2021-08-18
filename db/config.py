import os
import databases
import sqlalchemy


def get_database_path(mode) -> str:
    if mode and mode == "dev":
        return "sqlite:///./mydb.db"
    elif mode and mode == "prod":
        return "postgresql://postgres:postgres@127.0.0.1:5432/launcher_db"
    else:
        raise ValueError(
            f"APP_MODE is not valid, it should be `dev` or `prod`, got: `{mode}`"
        )


DATABASE_URL = get_database_path(os.getenv("APP_MODE"))

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)


def get_db():
    db = database
    try:
        yield db
    finally:
        db.close()
