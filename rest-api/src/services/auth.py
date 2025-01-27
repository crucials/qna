import os
from collections import namedtuple

from pymongo.errors import DuplicateKeyError
import jwt
import bcrypt

from mongo_database import accounts_collection


class UsernameAlreadyExistsError(ValueError):
    pass


class InvalidCredentialsError(ValueError):
    pass


SessionData = namedtuple("SessionData", ["token", "account"])


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
        except DuplicateKeyError:
            raise UsernameAlreadyExistsError()

        payload = {"account_id": new_account.inserted_id.__str__()}

        return SessionData(
            jwt.encode(payload, os.environ.get("JWT_SECRET_KEY"), algorithm="HS256"),
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
            jwt.encode(
                {"account_id": account["_id"].__str__()},
                os.environ.get("JWT_SECRET_KEY"),
            ),
            account,
        )


auth_service = AuthService()
