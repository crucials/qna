from bson import ObjectId
import flask
from marshmallow import RAISE
from werkzeug.exceptions import NotFound, BadRequest, Forbidden

from controllers.surveys.stats import survey_stats_controller_blueprint
from auth_middlewares import restrict_unauthorized_access
from errors.resource_not_found_error import ResourceNotFoundError
from models.account_dto import AccountDto
from models.survey import SurveyValidationSchema
from models.survey_response import SurveyResponseValidationSchema
from utils.convert_bson_to_json_dict import convert_bson_to_json_dict
from utils.decorators.api_response import api_response
from utils.get_account_from_headers import get_account_from_headers
from services.surveys import InvalidResponseDataError, surveys_service
from services.surveys.responses import survey_responses_service


surveys_controller_blueprint = flask.Blueprint(
    "surveys", __name__, url_prefix="/surveys"
)

surveys_controller_blueprint.register_blueprint(survey_stats_controller_blueprint)


@surveys_controller_blueprint.get("/<string:id>")
@api_response()
def get_survey_detailed_data(id: str):
    survey_data = surveys_service.get_survey_with_questions(id)

    if survey_data is None:
        raise NotFound("survey with specified id not found")

    return convert_bson_to_json_dict(survey_data)


@surveys_controller_blueprint.post("/")
@api_response()
def create_survey():
    restrict_unauthorized_access()

    account = get_account_from_headers(flask.request.headers)
    form = SurveyValidationSchema().loads(
        flask.request.get_data(as_text=True), many=False, unknown=RAISE
    )

    updated_account_dto = AccountDto.create_from_account_document(
        surveys_service.create_survey(account["_id"], form)
    )
    return convert_bson_to_json_dict(vars(updated_account_dto))


@surveys_controller_blueprint.delete("/<string:id>")
@api_response()
def delete_survey(id: str):
    restrict_unauthorized_access()

    account = get_account_from_headers(flask.request.headers)
    if not surveys_service.is_survey_owner(account, id):
        raise Forbidden("you can't delete this survey")

    surveys_service.delete_survey(id)

    return {}


@surveys_controller_blueprint.post("/<string:id>/responses")
@api_response()
def create_survey_response(id: str):
    survey_response = SurveyResponseValidationSchema().loads(
        flask.request.get_data(as_text=True), many=False, unknown=RAISE
    )

    try:
        survey_responses_service.create_survey_response(id, survey_response)
        return {}
    except InvalidResponseDataError as error:
        raise BadRequest(error.__str__())
    except ResourceNotFoundError:
        raise NotFound("survey not found")


@surveys_controller_blueprint.get("/<string:id>/responses")
@api_response()
def get_survey_responses(id: str):
    restrict_unauthorized_access()
    account = get_account_from_headers(flask.request.headers)

    if not ObjectId.is_valid(id):
        raise NotFound("survey not found")

    if not surveys_service.is_survey_owner(account, id):
        raise Forbidden("you can't access responses of this survey")

    return [
        convert_bson_to_json_dict(response)
        for response in survey_responses_service.get_survey_responses(id)
    ]
