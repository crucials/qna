import flask

from auth_middlewares import restrict_unauthorized_access
from utils.decorators.api_response import api_response


forms_controller_blueprint = flask.Blueprint('forms', __name__, url_prefix='/forms')

forms_controller_blueprint.before_request(restrict_unauthorized_access)


@forms_controller_blueprint.get('/')
@api_response()
def get_all_forms():
    print(flask.request.headers.get('Account'))
    return ['form1', 'form2']
