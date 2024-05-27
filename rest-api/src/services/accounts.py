from bson import ObjectId
from mongo_database import accounts_collection


class AccountsService:
    def get_account_by_id(self, id: str):
        return accounts_collection.find_one({
            '_id': ObjectId(id)
        })


accounts_service = AccountsService()
