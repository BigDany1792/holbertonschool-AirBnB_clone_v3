#!/usr/bin/python3
"""This module implement a rule that returns the status of the application"""
from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route("/status", strict_slashes=False)
def view_status():
    """View function that return a json message"""
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def view():
    """retrieves the number of each objects by type:"""
    return {
            "amenities": storage.count('Amenity'),
            "cities": storage.count('City'),
            "places": storage.count('Place'),
            "reviews": storage.count('Review'),
            "states": storage.count('State'),
            "users": storage.count('User')
            }
