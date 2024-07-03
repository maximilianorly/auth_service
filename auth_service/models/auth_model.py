import psycopg2

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