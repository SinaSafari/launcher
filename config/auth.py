import os

from pydantic import BaseModel


class AuthSettings(BaseModel):
    authjwt_secret_key = os.getenv(
        "JWT_SECRET", "dc5f32dd22dd0b294912d46c787f09491213fe264873c002d446b776132c1284"
    )
