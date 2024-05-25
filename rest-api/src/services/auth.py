import os

from pymongo.errors import DuplicateKeyError
import jwt
import bcrypt

from mongo_database import accounts_collection


class UsernameAlreadyExistsError(ValueError):
    pass


class InvalidCredentialsError(ValueError):
    pass


class AuthService:
    def sign_up(self, name: str, password: str):
        """
        ### Returns
        json web token
        """

        try:
            new_account = accounts_collection.insert_one({
                'name': name,
                'password': bcrypt.hashpw(password.encode(),
                                          bcrypt.gensalt(rounds=6))
            })
        except DuplicateKeyError:
            raise UsernameAlreadyExistsError()

        payload = {
            'account_id': new_account.inserted_id.__str__()
        }

        return jwt.encode(payload, os.environ.get('JWT_SECRET_KEY'), algorithm='HS256')

    def log_in(self, name: str, password: str):
        """
        ### Returns
        json web token
        """

        account = accounts_collection.find_one({ 'name': name })

        if account is None:
            raise InvalidCredentialsError()
        
        if not bcrypt.checkpw(password.encode(), account['password']):
            raise InvalidCredentialsError()

        return jwt.encode({ 'account_id': account['_id'].__str__() },
                          os.environ.get('JWT_SECRET_KEY'))


auth_service = AuthService()
