from controllers.auth import auth_controller_blueprint
from controllers.current_account import current_account_controller_blueprint
from controllers.surveys import surveys_controller_blueprint
from controllers.responses import responses_controller_blueprint


controllers_blueprints = [
    auth_controller_blueprint,
    current_account_controller_blueprint,
    surveys_controller_blueprint,
    responses_controller_blueprint,
]
