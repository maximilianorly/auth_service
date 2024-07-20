import psycopg2

from auth_service.models.utils.db_utils import end_cursor, get_cursor
from auth_service.models.utils.exceptions import DatabaseConnectionError

def create(clientId: str, clientSecret: str, isAdmin: bool):
    connection = None
    cursor = None
    query = "insert into clients (\"ClientId\", \"ClientSecret\", \"IsAdmin\") values(%s,%s,%s)"

    try:
        cursor, connection = get_cursor()
        cursor.execute(query, (clientId, clientSecret, isAdmin))
        connection.commit()

        return True
    except DatabaseConnectionError as error:
        raise
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error creating user", error)
        return None
    finally:
        end_cursor(cursor, connection)

def get_by_id(id: int):
    connection = None
    cursor = None
    query = f"SELECT * FROM clients WHERE \"Id\" = %s"

    try:
        cursor, connection = get_cursor()
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
    except DatabaseConnectionError as error:
        raise
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error getting user by ID", error)
        return None
    finally:
        end_cursor(cursor, connection)

def get_user_by_credentials(clientId, clientSecret):
    connection = None
    cursor = None
    query = "select * from clients where \"ClientId\"= %s and \"ClientSecret\"= %s"

    try:
        cursor, connection = get_cursor()
        cursor.execute(query, (clientId, clientSecret))
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
    except DatabaseConnectionError as error:
        raise
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error getting user from credentials", error)
        return None
    finally:
        end_cursor(cursor, connection)