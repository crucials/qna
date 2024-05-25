import flask

from utils.decorators.api_response import api_response


auth_controller_blueprint = flask.Blueprint('auth', __name__, url_prefix='/auth')


@auth_controller_blueprint.get('/sign-up')
@api_response()
def sign_up():
    return 'dasdadasd'
