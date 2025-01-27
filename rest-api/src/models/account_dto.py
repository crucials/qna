from dataclasses import dataclass
from typing import TypedDict

from models.survey import Survey


class Account(TypedDict):
    _id: str
    name: str
    surveys: list[Survey]


@dataclass(kw_only=True)
class AccountDto:
    _id: str
    name: str
    surveys: list

    @staticmethod
    def create_from_account_document(account: dict):
        fields_to_omit = ["password"]
        return AccountDto(
            **{key: account[key] for key in account.keys() if key not in fields_to_omit}
        )
