from functools import wraps
from flask import jsonify

from auth_service.routes.auth.utils.authorization_header import get_authorization_header, extract_token
from auth_service.routes.auth.utils.exceptions import AuthorizationHeaderMissing, InvalidToken, JWTDecodeError, TokenExpirationError
from auth_service.routes.auth.utils.jwt import decode_jwt
from auth_service.store.blacklist import is_token_blacklisted

def handle_auth_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        try:
            auth_header = get_authorization_header()
            token = extract_token(auth_header)

            if is_token_blacklisted(token):
                return jsonify({"success": False, "message": "Unauthorized (Blacklisted)"}), 401

            decoded = decode_jwt(token)
            if not decoded:
                return jsonify({"success": False, "message": "Unauthorized"}), 401

            # Pass the token and decoded token to the route function
            kwargs['token'] = token
            kwargs['decoded_token'] = decoded
            return func(*args, **kwargs)
        except AuthorizationHeaderMissing as e:
            return jsonify({"success": False, "message": str(e)}), 400
        except InvalidToken as e:
            return jsonify({"success": False, "message": str(e)}), 400
        except JWTDecodeError as e:
            return jsonify({"success": False, "message": str(e)}), 401
        except TokenExpirationError as e:
            return jsonify({"success": False, "message": str(e)}), 401
        except Exception as e:
            return jsonify({"success": False, "message": "An unexpected error occurred"}), 500
    return decorated_function