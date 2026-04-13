from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello from {os.getenv('ENV_NAME', 'UNKNOWN')} environment!"

app.run(host="0.0.0.0", port=5000)
