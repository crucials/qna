from bson import ObjectId
from pymongo import ReturnDocument

from mongo_database import accounts_collection


class FormsService:
    def create_form(self, account_id: ObjectId, form):
        form['_id'] = ObjectId()
        return accounts_collection.find_one_and_update({
            '_id': account_id
        }, {
            '$push': {
                'forms': form
            }
        }, return_document=ReturnDocument.AFTER)


forms_service = FormsService()
