"""
    Routes for the amenities blueprint.
"""

from flask import Blueprint
from src.controllers.amenities import (
    create_amenity,
    delete_amenity,
    get_amenity_by_id,
    get_amenities,
    update_amenity,
)

# Create a Blueprint for amenities with a URL prefix
amenities_bp = Blueprint("amenities", __name__, url_prefix="/amenities")
# Route to get all amenities
amenities_bp.route("/", methods=["GET"])(get_amenities)

# Route to create a new amenity
amenities_bp.route("/", methods=["POST"])(create_amenity)
# Route to get a specific amenity by ID
amenities_bp.route("/<string:amenity_id>", methods=["GET"])(get_amenity_by_id)
# Route to update a specific amenity by ID
amenities_bp.route("/<string:amenity_id>", methods=["PUT"])(update_amenity)
# Route to delete a specific amenity by ID
amenities_bp.route("/<string:amenity_id>", methods=["DELETE"])(delete_amenity)
