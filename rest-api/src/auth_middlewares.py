import os

import flask
import jwt
from werkzeug.datastructures import Headers
from werkzeug.exceptions import Unauthorized


def authorize_request():
    """
    this middleware registered on all routes by default

    gets account data from jwt in `Authorization` header and puts in
    `Account` header as json. if token is invalid, does nothing
    """

    token = flask.request.cookies.get('token')

    if token is None:
        return
    
    try:
        payload = jwt.decode(token, key=os.environ.get('JWT_SECRET_KEY'),
                             algorithms=['HS256'])

        if payload.get('account_id'):
            updated_headers = Headers(flask.request.headers)
            updated_headers.add('Account-Id', payload['account_id'])
            flask.request.headers = updated_headers
    except Exception as error:
        print(error)
        pass


def restrict_unauthorized_access():
    if flask.request.headers.get('Account-Id') is None:
        raise Unauthorized('invalid authorization header was specified')
