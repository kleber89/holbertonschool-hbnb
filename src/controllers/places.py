"""
Places controller
"""

from flask import abort, request
from src.models.place import Place

from flask import request, abort
from src.models.place import Place
from src.models.city import City
from src.models.user import User

def get_places():
    """Returns all places"""
    places: list[Place] = Place.get_all()
    return [place.to_dict() for place in places]

def create_place():
    """Creates a new place"""
    data = request.get_json()

    # Ensure the required fields are present
    required_fields = [
        'name', 'city_id', 'host_id', 'address', 'price_per_night', 
        'number_of_rooms', 'number_of_bathrooms', 'max_guests'
    ]
    for field in required_fields:
        if field not in data:
            abort(400, f"Missing field: {field}")

    try:
        place = Place.create(data)
    except ValueError as e:
        abort(400, str(e))

    return place.to_dict(), 201

def get_place_by_id(place_id: str):
    """Returns a place by ID"""
    place: Place | None = Place.get(place_id)
    
    if not place:
        abort(404, f"Place with ID {place_id} not found")

    return place.to_dict()

def update_place(place_id: str):
    """Updates a place by ID"""
    data = request.get_json()

    try:
        place: Place | None = Place.update(place_id, data)
    except ValueError as e:
        abort(400, str(e))

    if not place:
        abort(404, f"Place with ID {place_id} not found")

    return place.to_dict()

def delete_place(place_id: str):
    """Deletes a place by ID"""
    if not Place.delete(place_id):
        abort(404, f"Place with ID {place_id} not found")

    return "", 204