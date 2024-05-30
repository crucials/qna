import os

from dotenv import load_dotenv
from flask_cors import CORS
from marshmallow import ValidationError
from flask import Flask
from werkzeug.exceptions import HTTPException

from auth_middlewares import authorize_request
from controllers import controllers_blueprints


app = None


def create_flask_app():
    load_dotenv()

    app = Flask(__name__)
    app.url_map.strict_slashes = False

    CORS(app, origins=os.environ.get('FRONTEND_ORIGIN'))

    for blueprint in controllers_blueprints:
        app.register_blueprint(blueprint)

    @app.errorhandler(HTTPException)
    def send_json_error_response(error: HTTPException):
        return {
            'error': {
                'code': error.code,
                'explanation': error.description
            },
            'data': None,
        }, error.code or 500

    @app.errorhandler(ValidationError)
    def send_json_validation_error_response(error: ValidationError):
        invalid_fields = list(error.messages_dict)
        message = (error.messages_dict.get(invalid_fields[0])
                   or 'invalid request body')
        return {
            'error': {
                'code': 400,
                'field': invalid_fields[0],
                'explanation': message[0],
            },
            'data': None,
        }, 400

    app.before_request(authorize_request)

    return app
