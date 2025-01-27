import flask
from werkzeug.exceptions import BadRequest, InternalServerError, Conflict
from marshmallow import EXCLUDE

from models.account_dto import AccountDto
from models.account_credentials_schema import AccountCredentialsValidationSchema
from utils.convert_bson_to_json_dict import convert_bson_to_json_dict
from utils.decorators.api_response import api_response
from services.auth import (
    InvalidCredentialsError,
    UsernameAlreadyExistsError,
    auth_service,
)


TOKEN_COOKIE_MAX_AGE = 2592000

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
        return {
            "token": session.token,
            "account": convert_bson_to_json_dict(
                vars(AccountDto.create_from_account_document(session.account))
            ),
        }
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
        return {
            "token": session.token,
            "account": convert_bson_to_json_dict(
                vars(AccountDto.create_from_account_document(session.account))
            ),
        }
    except InvalidCredentialsError as error:
        raise BadRequest("invalid username or password") from error
