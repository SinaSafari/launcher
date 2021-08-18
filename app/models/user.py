import sqlalchemy
from db.config import metadata
from sqlalchemy import Integer, String

User = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", Integer, primary_key=True),
    sqlalchemy.Column("username", String(64), nullable=False),
    sqlalchemy.Column("password", String(128), nullable=False),
)
