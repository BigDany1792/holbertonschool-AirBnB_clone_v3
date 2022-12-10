#!/usr/bin/python3
"""
Module __init__
    instance: app_views
"""
from flask import Blueprint
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *

#  Create a Blueprint object called app_views
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
