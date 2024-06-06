from marshmallow import Schema, fields, validate


class SurveyResponseValidationSchema(Schema):
    name = fields.Str(required=True, allow_none=True,
                      validate=validate.Length(min=3, max=50))
    answers = fields.List(fields.Nested(lambda: AnswerValidationSchema()),
                          validate=validate.Length(min=1, max=30),
                          required=True)
    seconds_spent = fields.Int(required=True)


class AnswerValidationSchema(Schema):
    value = fields.Str(required=True, allow_none=True)
    question_id = fields.Str(required=True)
