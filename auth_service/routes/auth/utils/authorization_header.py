from flask import request
from auth_service.routes.auth.utils.exceptions import AuthorizationHeaderMissing, InvalidToken

def get_authorization_header():
    authorization_header = request.headers.get("Authorization")
    if not authorization_header:
        raise AuthorizationHeaderMissing("Invalid Authorization Header")
    return authorization_header

def extract_token(authorization_header):
    token = authorization_header.replace("Bearer ", "")
    if not token:
        raise InvalidToken("Invalid token supplied")
    return token