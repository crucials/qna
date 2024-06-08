from bson import ObjectId
from pymongo import ReturnDocument

from errors.survey_not_found_error import SurveyNotFoundError
from mongo_database import accounts_collection, questions_collection, responses_collection
from services.survey_stats import survey_stats_service


class RequiredResponseDataMissingError(Exception):
    pass


class SurveysService:
    def create_survey(self, account_id: ObjectId, survey):
        questions = survey.pop('questions')
        survey['_id'] = ObjectId()

        for question in questions:
            question['survey_id'] = survey['_id']

        questions_collection.insert_many(questions)

        survey_stats_service.create_initial_survey_stats(survey['_id'])

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
            raise RequiredResponseDataMissingError(
                'the name field must be specified'
            )
        
        for question in survey['questions']:
            answers = [answer for answer in response['answers']
                       if answer['question_id'] == question['_id'].__str__()
                       and answer['value'] is not None]
            
            if len(answers) == 0 and not question['optional']:
                raise RequiredResponseDataMissingError(
                    'some required questions\'s answers are missing'
                )
            
        response['survey_id'] = ObjectId(survey_id)
            
        responses_collection.insert_one(response)

    def get_survey_responses(self, survey_id: str):
        return list(responses_collection.find({'survey_id': ObjectId(survey_id)}))


surveys_service = SurveysService()
