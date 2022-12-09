#!/usr/bin/python3
"""
Module __init__
    instance: app_views
"""
from flask import Blueprint

#  Create a Blueprint object called app_views
app_views = Blueprint('app_views',__name__,url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
