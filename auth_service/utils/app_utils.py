import os

def is_app_running():
    return bool(int(os.getenv("RUNNING")))