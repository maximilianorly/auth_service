import os

class Config:
    RUNNING=0
    DEBUG = False
    DBNAME = os.getenv("POSTGRES_DB")
    DBUSER = os.getenv("POSTGRES_USER")
    DBPASSWORD = os.getenv("POSTGRES_PASSWORD")
    DBHOST = os.getenv("POSTGRES_HOST")
    DBPORT = os.getenv("POSTGRES_PORT")
    AUTHSECRET = os.getenv("AUTHSECRET")
    EXPIRESSECONDS = os.getenv("EXPIRESSECONDS")
    FLASK_RUN_PORT = os.getenv("FLASK_RUN_PORT", 5000)
    FLASK_APP = os.getenv("FLASK_APP")

class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = "development"

class ProductionConfig(Config):
    FLASK_ENV = "production"