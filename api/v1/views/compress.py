#!/usr/bin/python3
"""
Defines the view that compresses the uploaded image
"""
import os
from flask import jsonify
from flask import request
from flask import url_for
from flask import redirect
from flask import send_from_directory
from werkzeug.utils import secure_filename

from api.v1.views import app_views
from api.v1.config import Config
from compressor.run import execute
from compressor.config import DisplayConfiguration

config = Config()


def supported_formats(filename):
    """
    Checks if file format is supported
    """
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in config.ALLOWED_EXTENSIONS


@app_views.route('/compress', methods=['POST'])
def compress():
    """
    Recieves an image and compresses the image
    """
    if 'image' not in request.files:
        return jsonify({'message': 'No file in the request'}), 400
    if not request.is_json:
        return jsonify({'message': 'Payload is not a valid json'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'message': 'No file has been selected'}), 400
    if file and supported_formats(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(config.UPLOAD_FOLDER, filename)
        file.save(filepath)
        try:
            pay = request.get_json(silent=True)
            if pay is None:
                pay = {}
            execute(filepath, filepath, pay.get('quality', None),
                pay.get('width', None), pay.get('height', None),
                pay.get('keepExif', None), pay.get('grayScale', None),
                pay.get('compareSize', None), DisplayConfiguration('', '', True))
        except Exception as e:
            print(e)
            return jsonify({'message': 'Error encountered while processing request'}), 500
        else:
            return redirect(url_for('app_views.compressed_file', filename=filename))
    elif not file:
        return jsonify({'message': 'Upload a valid image file'}), 400
    else:
        return jsonify({'message': 'Image format is not supported'}), 400


@app_views.route('/compressed/<filename>')
def compressed_file(filename):
    """
    Sends compressed file for download
    """
    return send_from_directory(config.UPLOAD_FOLDER, filename)
