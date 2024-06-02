import bson
import bson.json_util
import flask

from auth_middlewares import restrict_unauthorized_access
from models.account_dto import AccountDto
from services.accounts import accounts_service
from utils.convert_bson_to_json_dict import convert_bson_to_json_dict
from utils.decorators.api_response import api_response
from utils.get_account_from_headers import get_account_from_headers
from controllers.current_account.forms import forms_controller_blueprint


current_account_controller_blueprint = flask.Blueprint('current-account', __name__,
                                                       url_prefix='/current-account')

current_account_controller_blueprint.before_request(restrict_unauthorized_access)

current_account_controller_blueprint.register_blueprint(forms_controller_blueprint)


@current_account_controller_blueprint.get('/')
@api_response()
def get_current_account():
    account = get_account_from_headers(flask.request.headers)

    return convert_bson_to_json_dict(
        vars(AccountDto.create_from_account_document(account))
    )

@current_account_controller_blueprint.delete('/')
@api_response()
def delete_account():
    account = get_account_from_headers(flask.request.headers)
    accounts_service.delete_account_by_id(account['_id'])
    
    return {}
