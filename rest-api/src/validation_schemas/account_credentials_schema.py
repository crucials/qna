import string

from marshmallow import Schema, fields, validate


class AccountCredentialsSchema(Schema):
    __alphanumeric_validation = validate.ContainsOnly(
        string.ascii_lowercase + string.digits + '_',
        error='only alphanumeric characters, digits and underscores are allowed'
    )
    
    name = fields.Str(required=True,
                      validate=[__alphanumeric_validation,
                                validate.Length(min=3, max=20)])
    password = fields.Str(required=True,
                          validate=validate.Length(min=5, max=30))
