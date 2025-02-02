import os

from dotenv import load_dotenv
from flask_cors import CORS
from marshmallow import ValidationError
from flask import Flask
from werkzeug.exceptions import HTTPException

from auth_middlewares import authorize_request
from controllers import controllers_blueprints
from limiter import limiter
from utils.create_validation_error_response import create_validation_error_response


app = None


def create_flask_app():
    global app

    load_dotenv()

    app = Flask(__name__)
    app.url_map.strict_slashes = False

    limiter.init_app(app)

    CORS(app, origins=os.environ.get("FRONTEND_ORIGIN"), supports_credentials=True)

    for blueprint in controllers_blueprints:
        app.register_blueprint(blueprint)

    @app.errorhandler(HTTPException)
    def send_json_error_response(error: HTTPException):
        return {
            "error": {"code": error.code, "explanation": error.description},
            "data": None,
        }, error.code or 500

    app.register_error_handler(ValidationError, create_validation_error_response)

    app.before_request(authorize_request)

    return app
