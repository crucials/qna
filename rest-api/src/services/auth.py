import os
import jwt

from mongo_database import accounts_collection


class AuthService:
    def sign_up(self, name: str, password: str):
        """
        ### Returns
        json web token
        """

        new_account = accounts_collection.insert_one({
            'name': name,
            'password': password
        })

        payload = {
            'account_id': new_account.inserted_id.__str__()
        }

        return jwt.encode(payload, os.environ.get('JWT_SECRET_KEY'))

    def log_in(self, name: str, password: str):
        """
        ### Returns
        json web token
        """
        print(f'logged in: {name}:{password}')
        return '1231543636'


auth_service = AuthService()
