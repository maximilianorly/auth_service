import hashlib

from flask import Blueprint, json, request, jsonify

from ..models import auth_model

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "password":
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@auth_bp.route("/client", methods=["POST","DELETE"])
def client():
    if request.method == "POST":

        # verify the token 
        # TODO after we create first credentials

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
def get_by_id(id: int):
    user = auth_model.get_by_id(id)
    
    if user:
        return jsonify({"success": True, "message": user}), 200
    else:
        return jsonify({"success": False, "message": "User not found"}), 404
