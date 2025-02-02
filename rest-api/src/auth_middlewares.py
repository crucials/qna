import logging

import bson.json_util
import bson
import flask
import jwt
from werkzeug.datastructures import Headers
from werkzeug.exceptions import Unauthorized

from services.accounts import accounts_service
from utils.auth.tokens import verify_access_token_and_get_payload


logger = logging.getLogger(__name__)


def authorize_request():
    """
    this middleware registered on all routes by default

    gets account data from jwt in `Authorization` header and puts it in
    `Account` header as json for request handlers. if token is invalid, does nothing
    """

    auth_header = flask.request.headers.get("Authorization")
    if auth_header is None:
        return

    auth_header_parts = auth_header.split(" ")

    if len(auth_header_parts) != 2:
        return

    if auth_header_parts[0] != "Bearer":
        return

    access_token = auth_header_parts[1]

    try:
        payload = verify_access_token_and_get_payload(access_token)
        account_id = payload.get("account_id")

        if not account_id:
            return

        account = accounts_service.get_account_by_id(account_id)

        if not account:
            return

        updated_headers = Headers(flask.request.headers)
        updated_headers.add("Account", bson.json_util.dumps(account))
        flask.request.headers = updated_headers
    except jwt.PyJWTError as error:
        logger.error(error)
        pass


def restrict_unauthorized_access():
    options_method_used = flask.request.method == "OPTIONS"
    if flask.request.headers.get("Account") is None and not options_method_used:
        raise Unauthorized("invalid authorization token was specified")
