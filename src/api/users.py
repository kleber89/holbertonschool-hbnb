"""
Routes the users blueprint.
"""

from flask import Blueprint
from src.controllers.users import (
    create_user,
    delete_user,
    get_user_by_id,
    get_users,
    update_user,
)

# Create a Blueprint for users with a URL prefix
users_bp = Blueprint("users", __name__, url_prefix="/users")

# Route to get all users
users_bp.route("/", methods=["GET"])(get_users)
# Route to create a new user
users_bp.route("/", methods=["POST"])(create_user)

# Route to get a specific user by ID
users_bp.route("/<string:user_id>", methods=["GET"])(get_user_by_id)
# Route to update a specific user by ID
users_bp.route("/<string:user_id>", methods=["PUT"])(update_user)
# Route to delete a specific user by ID
users_bp.route("/<string:user_id>", methods=["DELETE"])(delete_user)
