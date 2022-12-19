#!/usr/bin/python3
"""
Middleware: validates the incomcing request
"""
from flask import abort
from flask import request

from api.v1.config import Config


config = Config()


def supported_formats(filename):
    """
    Checks if file format is supported
    """
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in config.ALLOWED_EXTENSIONS


def validate_request():
    """
    Checks if request and payload are valid
    """
    if 'image' not in request.files:
        abort(400, description='No file in the request')
    if not request.is_json:
        abort(400, 'Payload is not a valid json')
    file = request.files['image']
    if file.filename == '':
        abort(400, 'No file has been selected')
    if not file:
        abort(400, 'Upload a valid image file')
    if not supported_formats(file.filename):
        abort(400, 'Image format is not supported')
