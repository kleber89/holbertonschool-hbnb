class Review(BaseModel):
    def __init__(self, id, text, rating, place, user):
        # ... existing code ...
        self.text = text  # Required
        self.rating = self.validate_rating(rating)  # Validate rating
        self.place = self.validate_place(place)  # Validate place
        self.user = self.validate_user(user)  # Validate user
        # ... existing code ...

    def validate_rating(self, rating):
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5.")
        return rating

    def validate_place(self, place):
        if not isinstance(place, Place):
            raise ValueError("Invalid place instance.")
        return place

    def validate_user(self, user):
        if not isinstance(user, User):
            raise ValueError("Invalid user instance.")
        return user

    # ... existing methods ...