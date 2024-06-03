import os
import socket

from flask import Flask
from routes.auth import auth_bp
from dotenv import load_dotenv

app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix='/auth')

@app.route('/')
def hello_world():
    return "Hello, World!"

# Searches for the next free port incementally from the input before returning
def find_free_port(start_port):
    port = start_port

    while True:
        print(f'Attempting to start port on {port}')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', port)) != 0:
                return port
            port += 1

if __name__ == '__main__':
    load_dotenv()
    default_port = int(os.getenv('FLASK_PORT', 5000))
    port = find_free_port(default_port)

    try:
        print(f"Running on port {port}")
        app.run(debug=True, host='0.0.0.0', port=port)
    except Exception as e:
        print(f"Failed to start server: {e}")
