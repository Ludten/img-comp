#!/usr/bin/python3
"""
Create an app instance
"""
import os
from flask import Flask
from flask import jsonify
from flasgger import Swagger

from api.v1.views import app_views
from api.v1.middy.app_views import validate_request 


app = Flask(__name__)

app.before_request_funcs = {
    "app_views": [validate_request]
}

app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(e):
    """
    Handling not found (404)
    Args:
        e: Exception
    Returns:
        JSON
    """
    status_code = str(e).split()[0]
    message = e.description if "Not found" in e.description else "Not found"
    return jsonify({"error": message}), status_code


@app.errorhandler(400)
def bad_request(e):
    """
    Handling bad request (400)
    Args:
        e: Exception
    Returns:
        JSON
    """
    status_code = str(e).split()[0]
    message = e.description
    return jsonify({"error": message}), status_code


@app.errorhandler(500)
def bad_request(e):
    """
    Handling server error (500)
    Args:
        e: Exception
    Returns:
        JSON
    """
    status_code = str(e).split()[0]
    message = e.description
    return jsonify({"error": message}), status_code


app.config['SWAGGER'] = {
    'title': 'Image Compressor Restful API'}

Swagger(app)


if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = os.getenv("PORT", 5000)
    app.run(host=host, port=port, threaded=True)
