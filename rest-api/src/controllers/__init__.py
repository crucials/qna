from controllers.auth import auth_controller_blueprint
from controllers.forms import forms_controller_blueprint


controllers_blueprints = [auth_controller_blueprint,
                          forms_controller_blueprint]
