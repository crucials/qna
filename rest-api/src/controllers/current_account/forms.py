import flask
from marshmallow import RAISE

from auth_middlewares import restrict_unauthorized_access
from models.account_dto import AccountDto
from utils.convert_bson_to_json_dict import convert_bson_to_json_dict
from utils.decorators.api_response import api_response
from services.forms import forms_service
from utils.get_account_from_headers import get_account_from_headers
from models.form import FormValidationSchema


forms_controller_blueprint = flask.Blueprint('forms', __name__, url_prefix='/forms')

forms_controller_blueprint.before_request(restrict_unauthorized_access)


@forms_controller_blueprint.post('/')
@api_response()
def create_form():
    account = get_account_from_headers(flask.request.headers)
    form = FormValidationSchema().loads(flask.request.get_data(as_text=True),
                                        many=False,
                                        unknown=RAISE)
    
    updated_account_dto = AccountDto.create_from_account_document(
        forms_service.create_form(account['_id'], form)
    )
    return convert_bson_to_json_dict(vars(updated_account_dto))
