from flask import current_app
import jwt

def verify_jwt(token):
    try:
        decoded = jwt.decode(token, current_app.config["AUTHSECRET"], algorithms=["HS256"])
        return decoded
    except (Exception) as error:
        print(error)
        return False