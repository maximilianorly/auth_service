import os

def get_connection_string():
    dbname = os.getenv("DBNAME")
    dbuser = os.getenv("DBUSER")
    dbpassword = os.getenv("DBPASSWORD")
    dbhost = os.getenv("DBHOST", "localhost")
    dbport = os.getenv("DBPORT", "5432")
    
    connection_string = f"dbname={dbname} user={dbuser} password={dbpassword} host={dbhost} port={dbport}"

    return connection_string