import os

from dotenv import load_dotenv
from flask import Flask
import waitress
from werkzeug.exceptions import HTTPException

from controllers import controllers_blueprints


load_dotenv()

app = Flask(__name__)
app.url_map.strict_slashes = False

for blueprint in controllers_blueprints:
    app.register_blueprint(blueprint)


@app.errorhandler(HTTPException)
def send_json_error_response(error: HTTPException):
    return {
        "error": {
            "code": error.code,
            "explanation": error.description
        },
        "data": None,
    }, error.code or 500


if os.environ.get('MODE') == 'DEV':
    app.run(port=8000)
else:
    print('running in production mode with waitress server')
    waitress.serve(app, port=8000)
