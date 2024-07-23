"""
Routes the places blueprint.
"""

from flask import Blueprint
from src.controllers.places import (
    create_place,
    delete_place,
    get_place_by_id,
    get_places,
    update_place,
)

# Create a Blueprint for places with a URL prefix
places_bp = Blueprint("places", __name__, url_prefix="/places")

# Route to get all places
places_bp.route("/", methods=["GET"])(get_places)
# Route to create a new place
places_bp.route("/", methods=["POST"])(create_place)

# Route to get a specific place by ID
places_bp.route("/<string:place_id>", methods=["GET"])(get_place_by_id)
# Route to update a specific place by ID
places_bp.route("/<string:place_id>", methods=["PUT"])(update_place)
# Route to delete a specific place by ID
places_bp.route("/<string:place_id>", methods=["DELETE"])(delete_place)
