#!/usr/bin/python3
"""
Basic API configurations
"""
from os.path import abspath, dirname, join

class Config:
    UPLOAD_FOLDER = join(dirname(abspath(__file__)), 'static', 'uploads')
    ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])
