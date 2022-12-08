#!/usr/bin/python3
"""
Module state
route:
    - route states
"""

from api.v1.views import app_views
from flask import abort, jsonify
from models import storage


@app_views.route('/states', strict_slashes=False)
@app_views.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """all object state"""
    list_json = []
    if id is not None:
        obj_id = storage.get("State", id)
        if obj_id is not None:
            list_json.append(obj_id.to_dict())
        else:
            abort(404)
    else:
        for obj in storage.all("State").values():
            list_json.append(obj.to_dict())
    return jsonify(list_json)
