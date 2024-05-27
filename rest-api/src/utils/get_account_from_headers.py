import bson
import bson.json_util
from werkzeug.datastructures import Headers
from werkzeug.exceptions import InternalServerError


def get_account_from_headers(headers: Headers):
    account = headers.get('Account')
    if not account:
        raise InternalServerError('failed to get your account info')
    
    return bson.json_util.loads(account)
