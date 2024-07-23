from datetime import datetime

class City:
    cities = []

    def __init__(self, name, country):
        self.id = len(City.cities) + 1
        self.name = name
        self.country = country
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # Ensure country is a Country instance
        if not isinstance(country, Country):
            raise TypeError("Country must be a Country instance")
        
        country.add_city(self)
        City.cities.append(self)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()