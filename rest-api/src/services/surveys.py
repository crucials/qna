from bson import ObjectId
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


surveys_service = SurveysService()
