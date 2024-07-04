from flask import current_app
import jwt

def encode_jwt(payload):
    try:
        encoded = jwt.encode(payload, current_app.config["AUTHSECRET"], algorithm="HS256")
        return encoded
    except (Exception) as error:
        print(error)
        return False


def decode_jwt(token):
    try:
        decoded = jwt.decode(token, current_app.config["AUTHSECRET"], algorithms=["HS256"])
        return decoded
    except (Exception) as error:
        print(error)
        return False
