"""
Routes the reviews blueprint.
"""

from flask import Blueprint
from src.controllers.reviews import (
    create_review,
    delete_review,
    get_review_by_id,
    get_reviews,
    update_review,
    get_reviews_from_place,
    get_reviews_from_user,
)

# Create a Blueprint for reviews with a URL prefix
reviews_bp = Blueprint("reviews", __name__, url_prefix="/reviews")

# Route to get all reviews
reviews_bp.route("/", methods=["GET"])(get_reviews)
# Route to create a new review
reviews_bp.route("/", methods=["POST"])(create_review)

# Route to get a specific review by ID
reviews_bp.route("/<string:review_id>", methods=["GET"])(get_review_by_id)
# Route to update a specific review by ID
reviews_bp.route("/<string:review_id>", methods=["PUT"])(update_review)
# Route to delete a specific review by ID
reviews_bp.route("/<string:review_id>", methods=["DELETE"])(delete_review)

# Route to get all reviews for a specific place
reviews_bp.route("/place/<string:place_id>", methods=["GET"])(get_reviews_from_place)
# Route to get all reviews by a specific user
reviews_bp.route("/user/<string:user_id>", methods=["GET"])(get_reviews_from_user)
