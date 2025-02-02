import logging

import flask
from werkzeug.exceptions import BadRequest, InternalServerError, Conflict, Unauthorized
from marshmallow import EXCLUDE

from models.account_dto import AccountDto
from models.account_credentials_schema import AccountCredentialsValidationSchema
from models.auth_providers import AuthProvider
from utils.auth.tokens import create_access_token, verify_refresh_token_and_get_payload
from utils.convert_bson_to_json_dict import convert_bson_to_json_dict
from utils.decorators.api_response import api_response
from utils.auth.google_oauth import (
    fetch_tokens_from_google_authorization_code,
    decode_google_id_token,
)
from services.auth import (
    InvalidCredentialsError,
    UsernameAlreadyExistsError,
    auth_service,
)


REFRESH_TOKEN_COOKIE_MAX_AGE_SECONDS = 60 * 60 * 24 * 30

logger = logging.getLogger(__name__)

auth_controller_blueprint = flask.Blueprint("auth", __name__, url_prefix="/auth")


@auth_controller_blueprint.post("/sign-up")
@api_response()
def sign_up():
    try:
        credentials = AccountCredentialsValidationSchema().loads(
            flask.request.get_data(as_text=True), many=False, unknown=EXCLUDE
        )

        if not isinstance(credentials, dict):
            raise InternalServerError()

        session = auth_service.sign_up(**credentials)

        response = flask.jsonify(
            {
                "access_token": session.access_token,
                "account": convert_bson_to_json_dict(
                    vars(AccountDto.create_from_account_document(session.account))
                ),
            }
        )

        response.set_cookie(
            "refresh-token",
            session.refresh_token,
            httponly=True,
            samesite="None",
            secure=True,
            max_age=REFRESH_TOKEN_COOKIE_MAX_AGE_SECONDS,
        )

        return response
    except UsernameAlreadyExistsError as error:
        raise Conflict("account with specified username already exists") from error


@auth_controller_blueprint.post("/log-in")
@api_response()
def log_in():
    try:
        credentials = AccountCredentialsValidationSchema().loads(
            flask.request.get_data(as_text=True), many=False, unknown=EXCLUDE
        )

        if not isinstance(credentials, dict):
            raise InternalServerError()

        session = auth_service.log_in(**credentials)

        response = flask.jsonify(
            {
                "access_token": session.access_token,
                "account": convert_bson_to_json_dict(
                    vars(AccountDto.create_from_account_document(session.account))
                ),
            }
        )

        response.set_cookie(
            "refresh-token",
            session.refresh_token,
            httponly=True,
            samesite="None",
            secure=True,
            max_age=REFRESH_TOKEN_COOKIE_MAX_AGE_SECONDS,
        )

        return response
    except InvalidCredentialsError as error:
        raise BadRequest("invalid username or password") from error


@auth_controller_blueprint.post("/access-token")
@api_response()
def get_new_access_token():
    refresh_token = flask.request.cookies.get("refresh-token")

    if refresh_token is None:
        raise Unauthorized("Refresh token cookie (`refresh-token`) is missing")

    try:
        refresh_token_payload: dict = verify_refresh_token_and_get_payload(
            refresh_token
        )
        refresh_token_payload.pop("exp")

        return create_access_token(refresh_token_payload)
    except Exception as error:
        raise Unauthorized("Refresh token is invalid") from error


@auth_controller_blueprint.post("/log-in/google")
@api_response()
def log_in_with_google():
    request_body = flask.request.json

    if request_body is None:
        raise BadRequest("Your request must have a json body")

    if not isinstance(request_body, dict) or "authorization_code" not in request_body:
        raise BadRequest("Your request body must have `authorization_code` field")

    code = request_body["authorization_code"]

    try:
        google_tokens = fetch_tokens_from_google_authorization_code(code)

        id_token_payload = decode_google_id_token(google_tokens["id_token"])

        new_session = auth_service.log_in_with_external_provider(
            id_token_payload["email"], AuthProvider.GOOGLE, id_token_payload["sub"]
        )

        response = flask.jsonify(
            {
                "access_token": new_session.access_token,
                "account": convert_bson_to_json_dict(
                    vars(AccountDto.create_from_account_document(new_session.account))
                ),
            }
        )

        response.set_cookie(
            "refresh-token",
            new_session.refresh_token,
            httponly=True,
            samesite="None",
            secure=True,
            max_age=REFRESH_TOKEN_COOKIE_MAX_AGE_SECONDS,
        )

        return response
    except Exception as error:
        logger.error(str(error))
        raise Unauthorized(
            "Log in failed, perhaps authorization code you passed is invalid"
        ) from error
