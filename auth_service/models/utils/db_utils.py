import os

import psycopg2

from auth_service.models.utils.exceptions import DatabaseConnectionError

def get_connection_string():
    dbname = os.getenv("DBNAME")
    dbuser = os.getenv("DBUSER")
    dbpassword = os.getenv("DBPASSWORD")
    dbhost = os.getenv("DBHOST", "localhost")
    dbport = os.getenv("DBPORT", "5432")
    
    connection_string = f"dbname={dbname} user={dbuser} password={dbpassword} host={dbhost} port={dbport}"

    return connection_string

def get_cursor():
    try:
        connection_string = get_connection_string()
        connection = psycopg2.connect(connection_string)
        return connection.cursor(), connection
    except Exception as error:
        print("Database connection error", error)
        raise DatabaseConnectionError("Database connection error")
    
def end_cursor(cursor, connection):
    try:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
    except Exception as error:
        print("Error closing database connection", error)
        raise DatabaseConnectionError("Error closing database connection")