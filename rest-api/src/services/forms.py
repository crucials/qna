from bson import ObjectId
from pymongo import ReturnDocument

from mongo_database import accounts_collection, questions_collection


class FormsService:
    def create_form(self, account_id: ObjectId, form):
        questions = form.pop('questions')
        form['_id'] = ObjectId()
        
        for question in questions:
            question['form_id'] = form['_id']
            question['type'] = question['type'].__str__()

        questions_insert_result = questions_collection.insert_many(questions)

        form['questions_ids'] = questions_insert_result.inserted_ids

        print(form)

        return accounts_collection.find_one_and_update({
            '_id': account_id
        }, {
            '$push': {
                'forms': form
            }
        }, return_document=ReturnDocument.AFTER)


forms_service = FormsService()
