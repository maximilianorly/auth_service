import os
from flask import Flask
from dotenv import load_dotenv
from auth_service.utils.app_utils import is_app_running
import config
from .routes.auth.auth import auth_bp
from .main import main_bp

def create_app():
    load_dotenv()
    app = Flask(__name__)

    env = os.getenv("FLASK_ENV", "development")

    if env == "production":
        print("creating prod")
        app.config.from_object(config.ProductionConfig)
    else:
        print("creating dev")
        app.config.from_object(config.DevelopmentConfig)

        if not (is_app_running()):
            # Run dynamic port setting only on start up, not reload
            from auth_service.utils.port_search import find_free_port
            free_port = find_free_port(int(app.config["FLASK_RUN_PORT"]))
            app.config["FLASK_RUN_PORT"] = free_port
            os.environ["FLASK_RUN_PORT"] = f"{free_port}"
            os.environ["RUNNING"] = "1"

    print(app.config)
    register_blueprints(app)

    return app

def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")