from datetime import datetime

class Amenity:
    amenities = []

    def __init__(self, name):
        self.id = len(Amenity.amenities) + 1
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        Amenity.amenities.append(self)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()