import flask
from werkzeug.exceptions import BadRequest, InternalServerError, Conflict
from marshmallow import EXCLUDE

from auth_middlewares import restrict_unauthorized_access
from utils.decorators.api_response import api_response
from services.auth import InvalidCredentialsError, UsernameAlreadyExistsError, auth_service
from utils.get_account_from_headers import get_account_from_headers
from validation_schemas.account_credentials_schema import AccountCredentialsSchema


TOKEN_COOKIE_MAX_AGE = 2592000

auth_controller_blueprint = flask.Blueprint('auth', __name__, url_prefix='/auth')


@auth_controller_blueprint.post('/sign-up')
@api_response()
def sign_up():
    try:
        credentials = AccountCredentialsSchema().loads(
            flask.request.get_data(as_text=True),
            many=False,
            unknown=EXCLUDE
        )

        if not isinstance(credentials, dict):
            raise InternalServerError()

        session = auth_service.sign_up(**credentials)
        return {
            'token': session.token,
            'account': session.account
        }
    except UsernameAlreadyExistsError:
        raise Conflict('account with specified username already exists')


@auth_controller_blueprint.post('/log-in')
@api_response()
def log_in():
    try:
        credentials = AccountCredentialsSchema().loads(
            flask.request.get_data(as_text=True),
            many=False,
            unknown=EXCLUDE
        )

        if not isinstance(credentials, dict):
            raise InternalServerError()

        session = auth_service.log_in(**credentials)
        return {
            'token': session.token,
            'account': session.account
        }
    except InvalidCredentialsError:
        raise BadRequest('invalid username or password')


@auth_controller_blueprint.get('/account')
@api_response()
def get_current_account():
    restrict_unauthorized_access()
    account = get_account_from_headers(flask.request.headers)

    return {
        'name': account['name']
    }
