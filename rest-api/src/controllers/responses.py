import flask
from werkzeug.exceptions import NotFound

from utils.convert_bson_to_json_dict import convert_bson_to_json_dict
from utils.decorators.api_response import api_response
from services.surveys.responses import survey_responses_service


responses_controller_blueprint = flask.Blueprint(
    "responses", __name__, url_prefix="/responses"
)


@responses_controller_blueprint.get("/<string:survey_response_id>")
@api_response()
def get_specific_response(survey_response_id: str):
    survey_response = survey_responses_service.get_response_by_id(survey_response_id)

    if survey_response is None:
        raise NotFound("response not found")

    return convert_bson_to_json_dict(survey_response)
