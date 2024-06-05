import flask
from marshmallow import RAISE
from werkzeug.exceptions import NotFound

from auth_middlewares import restrict_unauthorized_access
from models.account_dto import Account, AccountDto
from models.survey import SurveyValidationSchema
from utils.convert_bson_to_json_dict import convert_bson_to_json_dict
from utils.decorators.api_response import api_response
from utils.get_account_from_headers import get_account_from_headers
from services.surveys import surveys_service


surveys_controller_blueprint = flask.Blueprint('surveys', __name__,
                                               url_prefix='/surveys')


@surveys_controller_blueprint.get('/<string:id>')
@api_response()
def get_survey_detailed_data(id: str):
    print(id)

    survey_data = surveys_service.get_survey_with_questions(id)

    if survey_data is None:
        raise NotFound('survey with specified id not found')

    return convert_bson_to_json_dict(survey_data)


@surveys_controller_blueprint.post('/')
@api_response()
def create_survey():
    restrict_unauthorized_access()

    account = get_account_from_headers(flask.request.headers)
    form = SurveyValidationSchema().loads(flask.request.get_data(as_text=True),
                                        many=False,
                                        unknown=RAISE)

    updated_account_dto = AccountDto.create_from_account_document(
        surveys_service.create_survey(account['_id'], form)
    )
    return convert_bson_to_json_dict(vars(updated_account_dto))
