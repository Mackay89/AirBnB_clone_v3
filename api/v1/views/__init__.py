#!/usr/bin/python3
"""Script that inintialize views package."""
from flask import Blueprint

app_views = Blueprint('app_vw', __name__, url_prefix='/api/v1')

from api.v1.views.index import *

