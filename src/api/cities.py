"""
Routes the cities blueprint.
"""

from flask import Blueprint
from src.controllers.cities import (
    create_city,
    delete_city,
    get_city_by_id,
    get_cities,
    update_city,
)

# Create a Blueprint for cities with a URL prefix
cities_bp = Blueprint("cities", __name__, url_prefix="/cities")

# Route to get all cities
cities_bp.route("/", methods=["GET"])(get_cities)
# Route to create a new city
cities_bp.route("/", methods=["POST"])(create_city)

# Route to get a specific city by ID
cities_bp.route("/<string:city_id>", methods=["GET"])(get_city_by_id)
# Route to update a specific city by ID
cities_bp.route("/<string:city_id>", methods=["PUT"])(update_city)
# Route to delete a specific city by ID
cities_bp.route("/<string:city_id>", methods=["DELETE"])(delete_city)
