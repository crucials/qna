from dataclasses import dataclass
from typing import TypedDict

from marshmallow import Schema, fields, validate

from models.question_schema import QuestionValidationSchema


@dataclass
class FormDto:
    id: str
    title: str
    anonymous: bool

    @staticmethod
    def create_from_form_document(form):
        return FormDto(form['_id'].__str__(), form['title'], form['ano'])


class FormValidationSchema(Schema):
    title=fields.Str(required=True,validate=validate.Length(min=3, max=100))
    anonymous=fields.Bool(required=True)
    questions=fields.List(fields.Nested(lambda: QuestionValidationSchema()))
