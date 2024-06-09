import time
from bson import ObjectId
import flask
from werkzeug.exceptions import NotFound, Forbidden

from auth_middlewares import restrict_unauthorized_access
from utils.convert_bson_to_json_dict import convert_bson_to_json_dict
from utils.decorators.api_response import api_response
from services.surveys import surveys_service
from services.surveys.stats import survey_stats_service, StatsNotFoundError
from utils.get_account_from_headers import get_account_from_headers


survey_stats_controller_blueprint = flask.Blueprint('survey-stats', __name__,
                                                    url_prefix='/<string:id>/stats')


@survey_stats_controller_blueprint.put('/page-visits')
@api_response()
def increment_survey_visit_counter(id: str):
    try:
        survey_stats_service.increment_survey_visits_count(id)
    except StatsNotFoundError:
        raise NotFound('survey or its statistics not found')
    
    return {}


@survey_stats_controller_blueprint.get('/')
@api_response()
def get_survey_stats(id: str):
    restrict_unauthorized_access()
    account = get_account_from_headers(flask.request.headers)

    if not ObjectId.is_valid(id):
        raise NotFound('survey not found')

    if not surveys_service.is_survey_owner(account, id):
        raise Forbidden('you can\'t access stats for this survey')

    stats = survey_stats_service.get_survey_stats(id, include_responses_stats=True)

    if stats is None:
        raise NotFound('statistics not found')
    
    return convert_bson_to_json_dict(stats)
