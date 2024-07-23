"""
    Controller Country
"""

from flask import request, abort
from src.models.country import Country
from src.models.city import City


def get_countries():
    """Returns all countries"""
    countries: list[Country] = Country.get_all()
    return [country.to_dict() for country in countries]


def create_country():
    """Creates a new country"""
    data = request.get_json()

    # Ensure the required fields are present
    required_fields = ["name", "code"]
    for field in required_fields:
        if field not in data:
            abort(400, f"Missing field: {field}")

    try:
        country = Country.create(data["name"], data["code"])
    except ValueError as e:
        abort(400, str(e))

    return country.to_dict(), 201


def get_country_by_code(code: str):
    """Returns a country by code"""
    country: Country | None = Country.get(code)

    if not country:
        abort(404, f"Country with code {code} not found")

    return country.to_dict()


def get_country_cities(code: str):
    """Returns all cities in a country by country code"""
    country: Country | None = Country.get(code)

    if not country:
        abort(404, f"Country with code {code} not found")

    cities: list[City] = City.get_all_by_country_code(code)

    return [city.to_dict() for city in cities]
