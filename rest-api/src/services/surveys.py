from bson import ObjectId, is_valid
from pymongo import ReturnDocument

from mongo_database import accounts_collection, questions_collection


class SurveysService:
    def create_survey(self, account_id: ObjectId, survey):
        questions = survey.pop('questions')
        survey['_id'] = ObjectId()

        for question in questions:
            question['survey_id'] = survey['_id']

        questions_collection.insert_many(questions)

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
 

surveys_service = SurveysService()
