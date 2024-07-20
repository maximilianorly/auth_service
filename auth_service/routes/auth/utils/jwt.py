import jwt
from flask import current_app

from auth_service.routes.auth.utils.exceptions import JWTDecodeError, TokenExpirationError, InvalidToken

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
        raise JWTDecodeError(f"Failed to decode JWT: {error}")

def get_token_expiration(decoded):
    try:
        exp = decoded.get('exp')
        return exp
    except (Exception) as error:
        print(error)
        raise TokenExpirationError("Invalid Token supplied")

def extract_token(authorization_header):
    try:
        token = authorization_header.replace("Bearer ", "")
        return token
    except (Exception) as error:
        print(error)
        raise InvalidToken("Invalid Token supplied")