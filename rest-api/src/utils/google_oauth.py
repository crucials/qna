import os
from typing import TypedDict

import jwt
import requests


_GOOGLE_OAUTH_CLIENT_ID = os.environ["GOOGLE_OAUTH_CLIENT_ID"]
_GOOGLE_OAUTH_CLIENT_SECRET = os.environ["GOOGLE_OAUTH_CLIENT_SECRET"]
_GOOGLE_OAUTH_REDIRECT_URI = os.environ["GOOGLE_OAUTH_REDIRECT_URI"]

_GOOGLE_TOKEN_ISSUER = "https://accounts.google.com"
_GOOGLE_JWKS_URL = "https://www.googleapis.com/oauth2/v2/certs"
_GOOGLE_OAUTH_API_BASE_URL = "https://oauth2.googleapis.com"


class GoogleIdTokenPayload(TypedDict):
    email: str
    email_verified: bool
    sub: str
    picture: str
    name: str


def decode_google_id_token(id_token: str) -> GoogleIdTokenPayload:
    jwks_client = jwt.PyJWKClient(_GOOGLE_JWKS_URL)
    unverified_header = jwt.get_unverified_header(id_token)

    key = jwks_client.get_signing_key(unverified_header["kid"]).key

    return jwt.decode(
        id_token,
        algorithms=["RS256"],
        audience=_GOOGLE_OAUTH_CLIENT_ID,
        issuer=_GOOGLE_TOKEN_ISSUER,
        key=key,
    )


class GoogleTokenFetchError(Exception):
    pass


class GoogleTokensFetchResponse(TypedDict):
    access_token: str
    refresh_token: str
    id_token: str


def fetch_tokens_from_google_authorization_code(code: str) -> GoogleTokensFetchResponse:
    response = requests.post(
        f"{_GOOGLE_OAUTH_API_BASE_URL}/token",
        data={
            "code": code,
            "client_id": _GOOGLE_OAUTH_CLIENT_ID,
            "client_secret": _GOOGLE_OAUTH_CLIENT_SECRET,
            "grant_type": "authorization_code",
            "redirect_uri": _GOOGLE_OAUTH_REDIRECT_URI,
        },
    )

    if not response.ok:
        raise GoogleTokenFetchError(
            "Token exchange request failed "
            + f"with status code {response.status_code}: ${response.text}"
        )

    return response.json()
