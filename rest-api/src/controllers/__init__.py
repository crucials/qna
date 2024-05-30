from controllers.auth import auth_controller_blueprint
from controllers.forms import forms_controller_blueprint
from controllers.current_account import current_account_controller_blueprint


controllers_blueprints = [auth_controller_blueprint,
                          current_account_controller_blueprint,
                          forms_controller_blueprint]
