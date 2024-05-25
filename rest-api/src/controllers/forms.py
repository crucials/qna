from bson import ObjectId
import flask
from werkzeug.exceptions import InternalServerError

from auth_middlewares import restrict_unauthorized_access
from utils.decorators.api_response import api_response
from mongo_database import accounts_collection


forms_controller_blueprint = flask.Blueprint('forms', __name__, url_prefix='/forms')

forms_controller_blueprint.before_request(restrict_unauthorized_access)


@forms_controller_blueprint.get('/')
@api_response()
def get_all_forms():
    current_account = accounts_collection.find_one({
        '_id': ObjectId(flask.request.headers.get('Account-Id'))
    })

    if current_account is None:
        raise InternalServerError()

    return ['form1', 'form2', current_account['name']]
