from marshmallow import Schema, fields


class UserSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(rqquired=True)
    email = fields.Email(required=True)

