from enum import Enum
from typing import TypedDict

from marshmallow import Schema, fields, validate


class QuestionType(Enum):
    SHORT_TEXT = 'SHORT_TEXT'
    MULTILINE_TEXT = 'MULTILINE_TEXT'
    ONE_OPTION = 'ONE_OPTION'


class Question(TypedDict):
    text: str
    optional: bool
    type: QuestionType
    options: list[str]


class QuestionValidationSchema(Schema):
    text = fields.Str(required=True, validate=validate.Length(min=3, max=300))
    optional = fields.Bool(required=True)
    type = fields.Enum(QuestionType, required=True)

    options = fields.List(
        fields.Str(validate=validate.Length(min=1, max=150))
    )
