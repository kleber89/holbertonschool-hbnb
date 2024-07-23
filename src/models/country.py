from datetime import datetime

class Country:
    countries = []

    def __init__(self, name):
        self.id = len(Country.countries) + 1
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.cities = []

        Country.countries.append(self)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()

    def add_city(self, city):
        if city not in self.cities:
            self.cities.append(city)
