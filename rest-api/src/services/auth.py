from collections import namedtuple

from pymongo.errors import DuplicateKeyError
import bcrypt

from models.auth_providers import AuthProvider
from mongo_database import accounts_collection
from utils.auth.tokens import create_access_token


class UsernameAlreadyExistsError(ValueError):
    pass


class InvalidCredentialsError(ValueError):
    pass


SessionData = namedtuple("SessionData", ["access_token", "account"])


class AuthService:
    def sign_up(self, name: str, password: str):
        """
        ### Returns
        tuple with json token as the first item and account as the second one
        """

        try:
            new_account_dict = {
                "name": name,
                "password": bcrypt.hashpw(
                    password.encode(), bcrypt.gensalt(rounds=6)
                ).decode(),
                "surveys": [],
            }

            new_account = accounts_collection.insert_one(new_account_dict)
        except DuplicateKeyError as error:
            raise UsernameAlreadyExistsError() from error

        payload = {"account_id": str(new_account.inserted_id)}

        return SessionData(
            create_access_token(payload),
            new_account_dict,
        )

    def log_in(self, name: str, password: str):
        """
        ### Returns
        tuple with json token as the first item and account as the second one
        """

        account = accounts_collection.find_one({"name": name})

        if account is None:
            raise InvalidCredentialsError()

        if not bcrypt.checkpw(password.encode(), account["password"].encode()):
            raise InvalidCredentialsError()

        return SessionData(
            create_access_token(
                {"account_id": str(account["_id"])},
            ),
            account,
        )

    def log_in_with_external_provider(
        self, account_name: str, auth_provider: AuthProvider, external_account_id: str
    ):
        already_existing_account = accounts_collection.find_one(
            {
                "external_account_id": external_account_id,
                "auth_provider": auth_provider.value,
            }
        )

        if already_existing_account is not None:
            return SessionData(
                create_access_token(
                    {"account_id": str(already_existing_account["_id"])},
                ),
                already_existing_account,
            )

        new_account_dict = {
            "name": account_name,
            "surveys": [],
            "auth_provider": auth_provider.value,
            "external_account_id": external_account_id,
        }

        new_account = accounts_collection.insert_one(new_account_dict)

        payload = {"account_id": str(new_account.inserted_id)}
        return SessionData(
            create_access_token(payload),
            new_account_dict,
        )


auth_service = AuthService()
