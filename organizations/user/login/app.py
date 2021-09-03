import ujson
from marshmallow import ValidationError

from .utils import validator


def lambda_handler(event, context):
    try:
        body = ujson.loads(event['body'])
        result = validator.UserLoginSchema()
        res = not bool(result.validate(body))

        if res:
            return {
                "statusCode": 200,
                "body": ujson.dumps({
                    "message": "Welcome !",
                    "data": {
                        "token": result.load(body)['token']
                    }
                })
            }
        else:
            return {
                "statusCode": 400,
                "body": ujson.dumps({
                    "message": "Error !",
                    "data": result.load(body)
                })
            }
    except ValidationError as error:
        return {
            "statusCode": 400,
            "body": ujson.dumps({
                "message": error.messages
            })
        }
    except KeyError as error:
        return {
            "statusCode": 400,
            "body": ujson.dumps({
                "message": "Something went wrong. Unable to parse data !" + str(error)
            })
        }


def token_refresh(event, context):
    try:
        body = ujson.loads(event['body'])
        result = validator.RefreshTokenSchema()
        res = not bool(result.validate(body))

        if res:
            return {
                "statusCode": 200,
                "body": ujson.dumps({
                    "message": None,
                    "data": result.load(body)
                })
            }
        else:
            return {
                "statusCode": 400,
                "body": ujson.dumps({
                    "message": "Error !",
                    "data": result.validate(body)
                })
            }

    except ValidationError as error:
        return {
            "statusCode": 400,
            "body": ujson.dumps({
                "message": error.messages
            })
        }

    except KeyError:
        return {
            "statusCode": 400,
            "body": ujson.dumps({
                "message": "Something went wrong. Unable to parse data !"
            })
        }