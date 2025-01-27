from bson import ObjectId

from mongo_database import accounts_collection
from services.surveys import surveys_service


class AccountsService:
    def get_account_by_id(self, account_id: str):
        return accounts_collection.find_one({"_id": ObjectId(account_id)})

    def delete_account_by_id(self, account_id: str):
        deleted_account = accounts_collection.find_one_and_delete(
            {"_id": ObjectId(account_id)}
        )
        deleted_surveys_ids = [survey["_id"] for survey in deleted_account["surveys"]]

        surveys_service.delete_data_related_to_surveys(deleted_surveys_ids)


accounts_service = AccountsService()
