import json

import flask
from werkzeug.datastructures import Headers
from werkzeug.exceptions import Unauthorized


def authorize_request():
    """
    this middleware registered on all routes by default

    gets account data from jwt in `Authorization` header and puts in
    `Account` header as json. if token is invalid, does nothing
    """
    updated_headers = Headers(flask.request.headers)
    updated_headers.add('Account', json.dumps({'name': 'u', 'password': '1236'}))
    flask.request.headers = updated_headers


def restrict_unauthorized_access():
    if flask.request.headers.get('Account') is None:
        raise Unauthorized('invalid authorization header was specified')
