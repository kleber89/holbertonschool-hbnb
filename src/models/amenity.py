"""
Amenity Class
"""

from src.models.base import Base

class Amenity(Base):
    """Amenity representation"""

    name: str

    def __init__(self, name: str, **kwargs) -> None:
        """
        Initializes an Amenity instance.
        """
        super().__init__(**kwargs)
        self.name = name

    def __repr__(self) -> str:
        """
        String representation of the Amenity instance.
        """
        return f"<Amenity {self.id} ({self.name})>"

    def to_dict(self) -> dict:
        """
        Dictionary representation of the Amenity instance.
        """
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(data: dict) -> "Amenity":
        """
        Creates a new Amenity instance.
        """
        from src.persistence import repo

        amenity = Amenity(**data)
        repo.save(amenity)
        return amenity

    @staticmethod
    def update(amenity_id: str, data: dict) -> Optional["Amenity"]:
        """
        Updates an existing Amenity instance.
        """
        from src.persistence import repo

        amenity = Amenity.get(amenity_id)
        if not amenity:
            return None

        if "name" in data:
            amenity.name = data["name"]

        repo.update(amenity)
        return amenity

class PlaceAmenity(Base):
    """PlaceAmenity representation"""

    place_id: str
    amenity_id: str

    def __init__(self, place_id: str, amenity_id: str, **kwargs) -> None:
        """
        Initializes a PlaceAmenity instance.
        """
        super().__init__(**kwargs)
        self.place_id = place_id
        self.amenity_id = amenity_id

    def __repr__(self) -> str:
        """
        String representation of the PlaceAmenity instance.
        """
        return f"<PlaceAmenity ({self.place_id} - {self.amenity_id})>"

    def to_dict(self) -> dict:
        """
        Dictionary representation of the PlaceAmenity instance.
        """
        return {
            "id": self.id,
            "place_id": self.place_id,
            "amenity_id": self.amenity_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def get(place_id: str, amenity_id: str) -> Optional["PlaceAmenity"]:
        """
        Gets a PlaceAmenity object by place_id and amenity_id.
        """
        from src.persistence import repo

        place_amenities = repo.get_all("placeamenity")
        for place_amenity in place_amenities:
            if place_amenity.place_id == place_id and place_amenity.amenity_id == amenity_id:
                return place_amenity
        return None

    @staticmethod
    def create(data: dict) -> "PlaceAmenity":
        """
        Creates a new PlaceAmenity instance.
        """
        from src.persistence import repo

        new_place_amenity = PlaceAmenity(**data)
        repo.save(new_place_amenity)
        return new_place_amenity

    @staticmethod
    def delete(place_id: str, amenity_id: str) -> bool:
        """
        Deletes a PlaceAmenity object by place_id and amenity_id.
        """
        from src.persistence import repo

        place_amenity = PlaceAmenity.get(place_id, amenity_id)
        if not place_amenity:
            return False
        return repo.delete(place_amenity)
