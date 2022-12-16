#!/usr/bin/python3
"""
Create a Blueprint and define it's url_prefix
"""
from flask import  Blueprint

app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")

from api.v1.views.compress import *
