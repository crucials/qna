import json

import flask
from werkzeug.exceptions import BadRequest, InternalServerError
from marshmallow import EXCLUDE, ValidationError

from utils.decorators.api_response import api_response
from services.auth import auth_service
from validation_schemas.account_credentials_schema import AccountCredentialsSchema


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

        token = auth_service.sign_up(**credentials)

        response = flask.make_response()
        response.set_cookie('token', token)

        return response
    except ValidationError as error:
        error_messages = list(error.messages_dict)
        message = (error.messages_dict.get(error_messages[0])
                   or 'invalid request body')
        raise BadRequest(f'error in \'{error_messages[0]}\' field: \'{message[0]}\'')
    except json.JSONDecodeError:
        raise BadRequest('invalid json in request body')
