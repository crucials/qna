import datetime
from math import exp
import os

import jwt


_ACCESS_JWT_SECRET_KEY = os.environ["ACCESS_JWT_SECRET_KEY"]
_REFRESH_JWT_SECRET_KEY = os.environ["REFRESH_JWT_SECRET_KEY"]

_ACCESS_TOKEN_LIFETIME_MINUTES = 15
_REFRESH_TOKEN_LIFETIME_DAYS = 30

_JWT_ALGORITHM = "HS256"


def create_access_token(payload: dict):
    expiration_time = datetime.datetime.now() + datetime.timedelta(
        minutes=_ACCESS_TOKEN_LIFETIME_MINUTES
    )

    return jwt.encode(
        dict(**payload, exp=expiration_time),
        key=_ACCESS_JWT_SECRET_KEY,
        algorithm=_JWT_ALGORITHM,
    )


def verify_access_token_and_get_payload(access_token: str):
    return jwt.decode(access_token, key=_ACCESS_JWT_SECRET_KEY, algorithms=[_JWT_ALGORITHM])


def create_refresh_token(payload: dict):
    expiration_time = datetime.datetime.now() + datetime.timedelta(
        days=_REFRESH_TOKEN_LIFETIME_DAYS
    )

    return jwt.encode(
        dict(**payload, exp=expiration_time),
        key=_REFRESH_JWT_SECRET_KEY,
        algorithm=_JWT_ALGORITHM,
    )


def verify_refresh_token_and_get_payload(refresh_token: str):
    return jwt.decode(
        refresh_token, key=_REFRESH_JWT_SECRET_KEY, algorithms=[_JWT_ALGORITHM]
    )
