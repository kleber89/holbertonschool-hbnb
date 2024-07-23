"""
City class
"""

from typing import Any
from src.models.base import Base
from src.models.country import Country


class City(Base):

    name: str
    country_code: str

    def __init__(self, name: str, country_code: str, **kw) -> None:
        super().__init__(**kw)

        self.name = name
        self.country_code = country_code

    def __repr__(self) -> str:
        return super().__repr__()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "country_code": self.country_code,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(data: dict) -> "City":
        """
        Creates Cities.
        """
        from src.persistence import repo

        country = Country.get(data["country_code"])
        if not country:
            raise ValueError("Country not found")

        city = City(**data)
        repo.save(city)
        return city

    @staticmethod
    def update(city_id: str, data: dict) -> "City":
        """
        Updates an existing City instance.
        """
        from src.persistence import repo

        city = City.get(city_id)
        if not city:
            raise ValueError("City not found")

        for key, value in data.items():
            setattr(city, key, value)

        repo.update(city)
        return city
