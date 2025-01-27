from marshmallow import ValidationError

from utils.get_first_dict_key import get_first_dict_key


def create_validation_error_response(error: ValidationError):
    DEFAULT_ERROR_MESSAGE = "data you sent is invalid"

    first_invalid_field = get_first_dict_key(error.messages_dict)

    first_message = DEFAULT_ERROR_MESSAGE

    if first_invalid_field is not None:
        messages = error.messages_dict[first_invalid_field]

        if isinstance(messages, list):
            first_message = messages[0]

    return {
        "error": {
            "code": 400,
            "field": first_invalid_field,
            "explanation": first_message,
            "detailed_explanation": error.messages_dict,
        },
        "data": None,
    }, 400
