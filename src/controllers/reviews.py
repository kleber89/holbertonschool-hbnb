"""
Reviews controller
"""

from flask import abort, request
from src.models.review import Review


def get_reviews():
    """Returns all reviews"""
    reviews: list[Review] = Review.get_all()
    return [review.to_dict() for review in reviews]


def create_review():
    """Creates a new review"""
    data = request.get_json()

    # Ensure the required fields are present
    required_fields = ["place_id", "user_id", "comment", "rating"]
    for field in required_fields:
        if field not in data:
            abort(400, f"Missing field: {field}")

    try:
        # Validate rating is a float between 1 and 5
        rating = float(data["rating"])
        if not (1 <= rating <= 5):
            abort(400, "Rating must be between 1 and 5")

        # Check if the place and user exist
        if not Place.get(data["place_id"]):
            abort(400, f"Place with ID {data['place_id']} not found")
        if not User.get(data["user_id"]):
            abort(400, f"User with ID {data['user_id']} not found")

        review = Review.create(data)
    except ValueError as e:
        abort(400, str(e))
    except KeyError as e:
        abort(400, f"Missing field: {e}")

    return review.to_dict(), 201


def get_reviews_from_place(place_id: str):
    """Returns all reviews for a specific place"""
    # Check if the place exists
    if not Place.get(place_id):
        abort(404, f"Place with ID {place_id} not found")

    reviews: list[Review] = Review.get_all()  # Assuming this retrieves all reviews
    filtered_reviews = [
        review.to_dict() for review in reviews if review.place_id == place_id
    ]

    return filtered_reviews


def get_reviews_from_user(user_id: str):
    """Returns all reviews written by a specific user"""
    # Check if the user exists
    if not User.get(user_id):
        abort(404, f"User with ID {user_id} not found")

    reviews: list[Review] = Review.get_all()  # Assuming this retrieves all reviews
    filtered_reviews = [
        review.to_dict() for review in reviews if review.user_id == user_id
    ]

    return filtered_reviews


def get_review_by_id(review_id: str):
    """Returns a review by ID"""
    review: Review | None = Review.get(review_id)

    if not review:
        abort(404, f"Review with ID {review_id} not found")

    return review.to_dict()


def update_review(review_id: str):
    """Updates a review by ID"""
    data = request.get_json()

    try:
        review: Review | None = Review.update(review_id, data)
    except ValueError as e:
        abort(400, str(e))

    if not review:
        abort(404, f"Review with ID {review_id} not found")

    return review.to_dict()


def delete_review(review_id: str):
    """Deletes a review by ID"""
    if not Review.delete(review_id):
        abort(404, f"Review with ID {review_id} not found")

    return "", 204
