import os

import bson.json_util
import flask
import jwt
from werkzeug.datastructures import Headers
from werkzeug.exceptions import Unauthorized
import bson

from services.accounts import accounts_service


def authorize_request():
    """
    this middleware registered on all routes by default

    gets account data from jwt in `Authorization` header and puts it in
    `Account` header as json for request handlers. if token is invalid, does nothing
    """

    auth_header = flask.request.headers.get('Authorization')
    if auth_header is None:
        return

    auth_header_parts = auth_header.split(' ')

    if len(auth_header_parts) != 2:
        return

    if auth_header_parts[0] != 'Bearer':
        return

    token = auth_header_parts[1]

    try:
        payload = jwt.decode(token, key=os.environ.get('JWT_SECRET_KEY'),
                             algorithms=['HS256'])
        account_id = payload.get('account_id')

        if not account_id:
            return

        account = accounts_service.get_account_by_id(account_id)

        if not account:
            return

        updated_headers = Headers(flask.request.headers)
        updated_headers.add('Account', bson.json_util.dumps(account))
        flask.request.headers = updated_headers
    except Exception as error:
        print(error)
        pass


def restrict_unauthorized_access():
    if flask.request.headers.get('Account') is None:
        raise Unauthorized('invalid authorization token was specified')
