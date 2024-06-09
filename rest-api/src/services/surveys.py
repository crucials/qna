from bson import ObjectId
from pymongo import ReturnDocument

from errors.survey_not_found_error import SurveyNotFoundError
from models.account_dto import Account
from mongo_database import accounts_collection, questions_collection, responses_collection
from services.survey_stats import survey_stats_service
from utils.find_item import find_item


class InvalidResponseDataError(Exception):
    pass


class SurveysService:
    def create_survey(self, account_id: ObjectId, survey):
        questions = survey.pop('questions')
        survey['_id'] = ObjectId()

        for question in questions:
            question['survey_id'] = survey['_id']

        questions_collection.insert_many(questions)

        survey_stats_service.create_initial_survey_stats(survey['_id'], survey['title'])

        return accounts_collection.find_one_and_update({
            '_id': account_id
        }, {
            '$push': {
                'surveys': survey
            }
        }, return_document=ReturnDocument.AFTER)
    
    def get_survey_with_questions(self, id: str):
        if not ObjectId.is_valid(id):
            return None

        account_with_requested_survey = accounts_collection.find_one(
            {'surveys._id': ObjectId(id)},
            {'surveys.$': 1}
        )

        if account_with_requested_survey is None:
            return None
        
        survey =  account_with_requested_survey['surveys'][0]

        survey['questions'] = list(questions_collection.find({
            'survey_id': survey['_id']
        }))

        return survey
    
    def create_survey_response(self, survey_id: str, response):
        survey = self.get_survey_with_questions(survey_id)

        if survey is None:
            raise SurveyNotFoundError()
        
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

            answer['optional'] = answered_question['optional']
        
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
    
    def is_survey_owner(self, account: Account, survey_id: str):
        found_survey_on_account = find_item(
            account['surveys'],
            lambda survey: survey['_id'] == ObjectId(survey_id)
        )
        
        if found_survey_on_account is None:
            return False
        else:
            return True


surveys_service = SurveysService()
