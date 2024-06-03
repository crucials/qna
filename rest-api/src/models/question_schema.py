from enum import Enum
from typing import Literal, TypedDict, get_args

from marshmallow import Schema, fields, validate


QuestionType = Literal['SHORT_TEXT', 'MULTILINE_TEXT', 'ONE_OPTION', 'MULTIPLE_OPTION']
QUESTION_TYPES = get_args(QuestionType)


class Question(TypedDict):
    text: str
    optional: bool
    type: str
    options: list[str]


class QuestionValidationSchema(Schema):
    text = fields.Str(required=True, validate=validate.Length(min=3, max=300))
    optional = fields.Bool(required=True)
    type = fields.Str(required=True, validate=validate.OneOf(QUESTION_TYPES))

    options = fields.List(
        fields.Str(validate=validate.Length(min=1, max=150))
    )
