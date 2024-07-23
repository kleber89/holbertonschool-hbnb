""" 
Review class
"""

from src.models.base import Base
from src.models.place import Place
from src.models.user import User


class Review(Base):
    """Review representation"""

    place_id: str
    user_id: str
    comment: str
    rating: float

    def __init__(
        self, place_id: str, user_id: str, comment: str, rating: float, **kwargs
    ) -> None:
        """
        Initializes a Review instance.
        """
        super().__init__(**kwargs)
        self.place_id = place_id
        self.user_id = user_id
        self.comment = comment
        self.rating = rating

    def __repr__(self) -> str:
        """
        String representation of the Review instance.
        """
        return f"<Review {self.id} - '{self.comment[:25]}...'>"

    def to_dict(self) -> dict:
        """
        Dictionary representation of the Review instance.
        """
        return {
            "id": self.id,
            "place_id": self.place_id,
            "user_id": self.user_id,
            "comment": self.comment,
            "rating": self.rating,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(data: dict) -> "Review":
        """
        Creates a new Review instance.
        """
        from src.persistence import repo

        user = User.get(data["user_id"])
        if not user:
            raise ValueError(f"User with ID {data['user_id']} not found")

        place = Place.get(data["place_id"])
        if not place:
            raise ValueError(f"Place with ID {data['place_id']} not found")

        new_review = Review(**data)
        repo.save(new_review)
        return new_review

    @staticmethod
    def update(review_id: str, data: dict) -> "Review | None":
        """
        Updates an existing Review instance.
        """
        from src.persistence import repo

        review = Review.get(review_id)
        if not review:
            raise ValueError("Review not found")

        for key, value in data.items():
            setattr(review, key, value)

        repo.update(review)
        return review
