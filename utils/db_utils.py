import os

def get_connection_string():
    dbname = os.getenv('DBNAME')
    dbuser = os.getenv('DBUSER')
    dbpassword = os.getenv('DBPASSWORD')
    dbhost = os.getenv('DBHOST', 'localhost') # interestingly, second param is an optional fallback ^o^
    dbport = os.getenv('DBPORT', '5432')
    
    connection_string = f"postgresql://{dbuser}:{dbpassword}@{dbhost}:{dbport}/{dbname}"
    return connection_string