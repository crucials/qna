import flask
from marshmallow import RAISE

from auth_middlewares import restrict_unauthorized_access
from models.account_dto import AccountDto
from utils.convert_bson_to_json_dict import convert_bson_to_json_dict
from utils.decorators.api_response import api_response
from services.surveys import surveys_service
from utils.get_account_from_headers import get_account_from_headers
from models.survey_schema import SurveyValidationSchema


surveys_controller_blueprint = flask.Blueprint('surveys', __name__,
                                               url_prefix='/surveys')

surveys_controller_blueprint.before_request(restrict_unauthorized_access)


@surveys_controller_blueprint.post('/')
@api_response()
def create_survey():
    account = get_account_from_headers(flask.request.headers)
    form = SurveyValidationSchema().loads(flask.request.get_data(as_text=True),
                                        many=False,
                                        unknown=RAISE)

    updated_account_dto = AccountDto.create_from_account_document(
        surveys_service.create_survey(account['_id'], form)
    )
    return convert_bson_to_json_dict(vars(updated_account_dto))
