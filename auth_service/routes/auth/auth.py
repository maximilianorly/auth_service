import hashlib

from flask import Blueprint, request, jsonify, current_app

from auth_service.models.utils.exceptions import DatabaseConnectionError
from auth_service.routes.auth.utils.authorization_header import extract_token, get_authorization_header
from auth_service.routes.auth.utils.decorators import handle_auth_required, handle_database_exceptions
from auth_service.routes.auth.utils.jwt import encode_jwt, decode_jwt, get_token_expiration 

from auth_service.routes.auth.utils.exceptions import AuthorizationHeaderMissing, InvalidToken, JWTDecodeError, TokenExpirationError

from auth_service.store.blacklist import blacklist_token, is_token_blacklisted

from ...models import auth_model

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/client", methods=["POST","DELETE"])
@handle_database_exceptions
def client():
    if request.method == "POST":
        # get the client_id and secret from the client application
        client_id = request.form.get("client_id")
        client_secret_input = request.form.get("client_secret")
        is_admin = request.form.get("is_admin")        

        # the client secret in the database is "hashed" with a one-way hash
        hash_object = hashlib.sha1(bytes(client_secret_input, "utf-8"))
        hashed_client_secret = hash_object.hexdigest()

        createResponse = auth_model.create(client_id, hashed_client_secret, is_admin)

        if createResponse:
            return jsonify({"success": True, "message": "Successfully created user"}), 200
        else:
            return jsonify({"success": False, "message": "Could not create user"}), 409

    elif request.method == "DELETE":
        # not yet implemented
        return jsonify({"success": False, "message": "Method not implemented"}), 501


@auth_bp.route(f"/client/<int:id>", methods=["GET"])
@handle_auth_required
@handle_database_exceptions
def get_by_id(id: int, token, decoded_token):
    user = auth_model.get_by_id(id)
    
    if user:
        return jsonify({"success": True, "message": user}), 200
    else:
        return jsonify({"success": False, "message": "User not found"}), 404


@auth_bp.route("/authenticate", methods=["POST"])
@handle_database_exceptions
def auth():
    client_id = request.form.get("client_id")
    client_secret_input = request.form.get("client_secret")

    # Hash client secret with the same hash as in DB
    hash_object = hashlib.sha1(bytes(client_secret_input, "utf-8"))
    hashed_client_secret = hash_object.hexdigest()

    user = auth_model.get_user_by_credentials(client_id, hashed_client_secret)

    if user:
        from auth_service.routes.auth.utils.auth_payload import auth_payload
        from auth_service.routes.auth.utils.auth_response import auth_response

        payload = auth_payload(user['id'], user['client_id'], user['is_admin'])            
        encoded_jwt = encode_jwt(payload)

        response = auth_response(encoded_jwt, current_app.config["EXPIRESSECONDS"], user["is_admin"])
        return response
    else:
        return jsonify({"success": False, "message": "User not found"}), 404

@auth_bp.route("/verify-jwt", methods=["POST"])
@handle_auth_required
def verify(token, decoded_token):
    return jsonify({"success": True, "message": decoded_token }), 200
    
@auth_bp.route("/logout", methods=["POST"])
@handle_auth_required
def logout(token, decoded_token):
    exp = get_token_expiration(decoded_token)
    success = blacklist_token(token, exp)

    if success:
        return jsonify({"success": True, "message": "Successfully logged out user"}), 200
    else:
        return jsonify({"success": False, "message": "Failed to log user out"}), 500
    