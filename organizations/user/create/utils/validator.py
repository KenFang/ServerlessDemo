from argon2 import PasswordHasher
from marshmallow import Schema, fields, post_load, ValidationError
from create.utils import db


# Takes plain-text password and returns encrypted password
def encrypt(plain_text_password):
    ph = PasswordHasher()
    hashed_password = ph.hash(plain_text_password)
    return hashed_password


class UserRegistrationSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(rqquired=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)

    @post_load
    def encrypt_password(self, data, **kwargs):
        data["password"] = encrypt(data["password"])
        return data

    @post_load
    def validate_email(self, data, **kwargs):
        mongo = db.MongoDBConnection()
        with mongo:
            database = mongo.connection["myDB"]
            collection = database["registrations"]

            # check email already exists in DB. If true
            # raise validation error.
            if collection.find_one({"email": data["email"]}) is not None:
                raise ValidationError('This email address is already taken.')

        return data
