class Place(BaseModel):
    def __init__(self, id, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.id = id  # Unique identifier
        self.title = self.validate_title(title)  # Validate title
        self.description = description  # Optional
        self.price = self.validate_price(price)  # Validate price
        self.latitude = self.validate_latitude(latitude)  # Validate latitude
        self.longitude = self.validate_longitude(longitude)  # Validate longitude
        self.owner = self.validate_owner(owner)  # Validate owner
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    def validate_title(self, title):
        if not title or len(title) > 100:
            raise ValueError("Title is required and must be a maximum of 100 characters.")
        return title

    def validate_price(self, price):
        if price <= 0:
            raise ValueError("Price must be a positive value.")
        return price

    def validate_latitude(self, latitude):
        if latitude < -90.0 or latitude > 90.0:
            raise ValueError("Latitude must be between -90.0 and 90.0.")
        return latitude

    def validate_longitude(self, longitude):
        if longitude < -180.0 or longitude > 180.0:
            raise ValueError("Longitude must be between -180.0 and 180.0.")
        return longitude

    def validate_owner(self, owner):
        if not isinstance(owner, User):
            raise ValueError("Invalid owner instance.")
        return owner

    # ... existing methods ...