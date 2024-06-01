from dataclasses import dataclass

from models.form import FormDto


@dataclass
class AccountDto:
    name: str
    forms: list[FormDto]

    @staticmethod
    def create_from_account_document(account):
        return AccountDto(
            account['name'],
            [FormDto.create_from_form_document(form) for form in account['forms']]
        )
