#!/usr/bin/python3
"""routes /reviews"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.user import User
from models.place import Place
from models.review import Review
from models import storage


@app_views.route('/places/<string:place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_reviews_from_places(places_id):
    """Method that retrieve a list of all reviews by id"""
    place = storage.get(Place, places_id)
    if (place is None):
        abort(404)

    return (jsonify([review.to_dict() for review in place.reviews]))


@app_views.route('/reviews/<string:review_id>', methods=['GET'],
                 strict_slashes=False)
def get_review_id(review_id):
    """Method that retrieve a list of all reviews by id"""
    review = storage.get(Review, review_id)
    if (review is None):
        abort(404)
    return (jsonify(review.to_dict()))


@app_views.route('/reviews/<string:review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_review(review_id):
    """Method that delete a review by id"""
    review = storage.get(Review, review_id)
    if (review is None):
        abort(404)
    review.delete()
    storage.save()

    return jsonify({}, 200)


@app_views.route('/places/<string:place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def post_review(place_id):
    """Method that post a new review"""
    place = storage.get(Place, place_id)
    if (place is None):
        abort(404)
    res = request.get_json()
    if (type(res) != dict):
        abort(400, description="Not a JSON")
    if (not res.get("user_id")):
        abort(400, description="Missing user_id")
    res['place_id'] = place_id
    user = storage.get(User, res.get('user_id'))
    if user is None:
        abort(404)
    if not res.get("text"):
        abort(400, description="Missing text")
    new_review = Review(**res)
    new_review.place_id = place_id
    new_review.save()
    return (jsonify(new_review.to_dict()), 201)


@app_views.route('/reviews/<string:review_id>', methods=['PUT'],
                 strict_slashes=False)
def put_review(review_id):
    """Method to update/put a review by id"""
    find_review = storage.get(Review, review_id)
    if (find_review is None):
        abort(404)

    update_review = request.get_json(silent=True)
    if (type(update_review) is dict):
        update_review.pop('id', None)
        update_review.pop('user_id', None)
        update_review.pop('place_id', None)
        update_review.pop('created_at', None)
        update_review.pop('updated_at', None)

        for key, value in update_review.items():
            setattr(find_review, key, value)
        find_review.save()
        return (jsonify(find_review.to_dict()), 200)

    return (jsonify({'message': 'Not a JSON'}), 400)
