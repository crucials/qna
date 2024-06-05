from typing import TypedDict
from marshmallow import Schema, fields, validate

from models.question import Question, QuestionValidationSchema


class Survey(TypedDict):
    _id: str
    title: str
    anonymous: bool
    questions: list[Question]


class SurveyValidationSchema(Schema):
    title = fields.Str(required=True, validate=validate.Length(min=3, max=100))
    anonymous = fields.Bool(required=True)
    questions = fields.List(fields.Nested(lambda: QuestionValidationSchema()),
                            validate=validate.Length(1, 30))
