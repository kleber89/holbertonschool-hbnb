from datetime import datetime

class Place:
    places = []

    def __init__(self, name, host, latitude, longitude, price_per_night, max_guests):
        self.id = len(Place.places) + 1
        self.name = name
        self.host = host
        self.latitude = latitude
        self.longitude = longitude
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.amenities = []
        
        # Ensure host is a User instance
        if not isinstance(host, User):
            raise TypeError("Host must be a User instance")
        
        Place.places.append(self)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()

    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)