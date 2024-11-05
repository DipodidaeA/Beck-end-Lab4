from flask import jsonify
from datetime import datetime
from . import app

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    response = {
        "status": "200",
        "date": datetime.utcnow().isoformat()
    }
    return jsonify(response), 200