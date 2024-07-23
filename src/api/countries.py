"""
Routes the countries blueprint.
"""

from flask import Blueprint
from src.controllers.countries import (
    create_country,
    get_country_by_code,
    get_country_cities,
)

# Create a Blueprint for countries with a URL prefix
countries_bp = Blueprint("countries", __name__, url_prefix="/countries")

# Route to get a specific country by ID
countries_bp.route("/<string:country_id>", methods=["GET"])(get_country_by_code)
# Route to get all cities within a specific country
countries_bp.route("/<string:country_id>/cities", methods=["GET"])(get_country_cities)
