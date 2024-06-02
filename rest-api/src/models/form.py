from marshmallow import Schema, fields, validate

from models.question_schema import QuestionValidationSchema


class FormValidationSchema(Schema):
    title=fields.Str(required=True,validate=validate.Length(min=3, max=100))
    anonymous=fields.Bool(required=True)
    questions=fields.List(fields.Nested(lambda: QuestionValidationSchema()))
