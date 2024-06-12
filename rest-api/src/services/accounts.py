from bson import ObjectId
from mongo_database import (accounts_collection, questions_collection,
                            responses_collection, survey_stats_collection)


class AccountsService:
    def get_account_by_id(self, id: str):
        return accounts_collection.find_one({
            '_id': ObjectId(id)
        })

    def delete_account_by_id(self, id: str):
        deleted_account = accounts_collection.find_one_and_delete({
            '_id': ObjectId(id)
        })
        deleted_surveys_ids = [survey['_id'] for survey in deleted_account['surveys']]

        questions_collection.delete_many({
            'survey_id': {'$in': deleted_surveys_ids}
        })
        
        responses_collection.delete_many({
            'survey_id': {'$in': deleted_surveys_ids}
        })

        survey_stats_collection.delete_many({
            'survey_id': {'$in': deleted_surveys_ids}
        })


accounts_service = AccountsService()
