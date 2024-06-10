from bson import ObjectId

from errors.resource_not_found_error import ResourceNotFoundError
from mongo_database import responses_collection
from services.surveys import InvalidResponseDataError, surveys_service
from utils.find_item import find_item


class SurveyResponsesService:
    def create_survey_response(self, survey_id: str, response):
        survey = surveys_service.get_survey_with_questions(survey_id)

        if survey is None:
            raise ResourceNotFoundError()

        if response.get('name') is None and not survey['anonymous']:
            raise InvalidResponseDataError(
                'the name field must be specified'
            )

        for answer in response['answers']:
            answer['question_id'] = ObjectId(answer['question_id'])

            answered_question = find_item(
                survey['questions'],
                lambda question: answer['question_id'] == question['_id']
            )

            if answered_question is None:
                raise InvalidResponseDataError('some questions cant be found')

            answer['question'] = answered_question

        for question in survey['questions']:
            answers = [
                answer for answer in response['answers']
                if answer['question_id'] == question['_id']
                and answer['value'] is not None
            ]

            if len(answers) == 0 and not question['optional']:
                raise InvalidResponseDataError(
                    'some required questions\'s answers are missing'
                )

        response['survey_id'] = ObjectId(survey_id)

        responses_collection.insert_one(response)

    def get_survey_responses(self, survey_id: str):
        return list(responses_collection.find({'survey_id': ObjectId(survey_id)}))

    def get_response_by_id(self, id: str):
        if not ObjectId.is_valid(id):
            return None

        return responses_collection.find_one({'_id': ObjectId(id)})


survey_responses_service = SurveyResponsesService()
