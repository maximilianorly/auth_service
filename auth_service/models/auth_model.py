from flask import current_app
import jwt
import psycopg2

from auth_service.routes.auth.utils.jwt import encode_jwt

from ..utils.db_utils import get_connection_string

connection_string = get_connection_string()

def create(clientId: str, clientSecret: str, isAdmin: bool):
    connection = None
    query = "insert into clients (\"ClientId\", \"ClientSecret\", \"IsAdmin\") values(%s,%s,%s)"

    try:
        connection = psycopg2.connect(connection_string)
        cursor = connection.cursor()

        cursor.execute(query, (clientId, clientSecret, isAdmin))
        connection.commit()

        return True
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        if connection is not None:
            cursor.close()
            connection.close()

        return False
    finally:
        if connection is not None:
            cursor.close()
            connection.close()

def get_by_id(id: int):
    connection = None
    query = f"SELECT * FROM clients WHERE \"Id\" = %s"

    try:
        connection = psycopg2.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute(query, (id,))
        user = cursor.fetchone()
        
        if user:
            # Convert the user data to a dictionary
            user_data = {
                "id": user[0],
                "client_id": user[1],
                "client_secret": user[2],
                "is_admin": user[3]
            }

            return user_data
        else:
            return None
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        if connection is not None:
            cursor.close()
            connection.close()

            return None
    finally:
        if connection is not None:
            cursor.close()
            connection.close()

def authenticate(clientId, clientSecret):
    connection = None
    query = "select * from clients where \"ClientId\"= %s and \"ClientSecret\"= %s"

    try:
        connection = psycopg2.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute(query, (clientId, clientSecret))
        rows = cursor.fetchall()
        isAdmin = False

        if cursor.rowcount == 1:
            from auth_service.routes.auth.utils.auth_payload import auth_payload
            from auth_service.routes.auth.utils.auth_response import auth_response

            for row in rows:
                isAdmin = row[3]
                payload = auth_payload(row[0],row[1], isAdmin)
                break

            encoded_jwt = encode_jwt(payload)

            response = auth_response(encoded_jwt, current_app.config["EXPIRESSECONDS"], isAdmin)


            return response
        else:
            return False

    except (Exception, psycopg2.DatabaseError) as error:

        print(error)
        if connection is not None:
            cursor.close()
            connection.close()

        return False

    finally:
        if connection is not None:
            cursor.close()
            connection.close()