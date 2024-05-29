from dataclasses import dataclass


@dataclass
class AccountDto:
    name: str

    @staticmethod
    def create_from_account_document(account):
        return AccountDto(account['name'])
