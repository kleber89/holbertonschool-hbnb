from datetime import datetime

class Review:
    reviews = []

    def __init__(self, place, user, text):
        self.id = len(Review.reviews) + 1
        self.place = place
        self.user = user
        self.text = text
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # Ensure place and user are instances of Place and User
        if not isinstance(place, Place):
            raise TypeError("Place must be a Place instance")
        if not isinstance(user, User):
            raise TypeError("User must be a User instance")

        Review.reviews.append(self)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()