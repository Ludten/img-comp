#!/usr/bin/python3
"""
Defines the view that compresses the uploaded image
"""
import os
from flask import abort
from flask import jsonify
from flask import request
from flask import url_for
from flask import redirect
from flask import send_from_directory
from flasgger import swag_from
from werkzeug.utils import secure_filename

from api.v1.views import app_views
from api.v1.config import Config
from compressor.run import execute
from compressor.config import DisplayConfiguration

config = Config()


@app_views.route('/compress', methods=['POST'])
@swag_from('doc/compress.yaml')
def compress():
    """
    Recieves an image and compresses the image
    """
    file = request.files['image']
    filename = secure_filename(file.filename)
    filepath = os.path.join(config.UPLOAD_FOLDER, filename.lower())
    file.save(filepath)
    try:
        pay = request.get_json(silent=True)
        if pay is None:
            pay = {}
        execute(filepath, filepath, pay.get('quality', None),
            pay.get('width', None), pay.get('height', None),
            pay.get('keepExif', None), False, pay.get('grayScale', None),
            pay.get('compareSize', None), DisplayConfiguration('', '', True))
    except Exception:
        return jsonify({'message': 'Error encountered while processing request'}), 500
    return redirect(url_for('app_views.compressed_file', filename=filename))


@app_views.route('/convert/png-to-jpeg', methods=['POST'])
@swag_from('doc/compress.yaml')
def convert():
    """
    Recieves an image and compresses the image
    """
    file = request.files['image']
    filename = secure_filename(file.filename)
    extension = filename.rsplit('.')[-1]
    if not isinstance(extension, str) or extension.upper() != 'PNG':
        abort(400, "Image is not in PNG format")
    filepath = os.path.join(config.UPLOAD_FOLDER, filename.lower())
    file.save(filepath)
    try:
        pay = request.get_json(silent=True)
        if pay is None:
            pay = {}
        execute(filepath, filepath, pay.get('quality', None),
            pay.get('width', None), pay.get('height', None),
            pay.get('keepExif', None), True, pay.get('grayScale', None),
            pay.get('compareSize', None), DisplayConfiguration('', '', True))
    except Exception:
        abort(500, 'Error encountered while processing request')
    return redirect(url_for('app_views.compressed_file', filename=filename.replace('png', 'jpg')))


@app_views.route('/compressed/<filename>')
def compressed_file(filename):
    """
    Sends compressed file for download
    """
    return send_from_directory(config.UPLOAD_FOLDER, filename)
