#!/usr/bin/python3
""" Method that starts a Flask web application """
from api.v1.views import app_views
from flask import Flask
from flask import jsonify
from flask import make_response
from models import storage
import os

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def close(self):
    """ this method logs out the database session """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ Error 404 """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(
            host=os.getenv("HBNB_API_HOST", '0.0.0.0'),
            port=os.getenv("HBNB_API_PORT", 5000),
            threaded=True,
            debug=True
           )
# app.config["DEBUG"] = True
