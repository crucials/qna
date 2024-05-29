import flask

from auth_middlewares import restrict_unauthorized_access
from utils.decorators.api_response import api_response
from mongo_database import accounts_collection
from utils.get_account_from_headers import get_account_from_headers


forms_controller_blueprint = flask.Blueprint('forms', __name__, url_prefix='/forms')

forms_controller_blueprint.before_request(restrict_unauthorized_access)


@forms_controller_blueprint.get('/')
@api_response()
def get_all_forms():
    return ['form1', 'form2']
