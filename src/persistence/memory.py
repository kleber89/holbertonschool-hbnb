"""
    Lst
"""

from datetime import datetime
from typing import Dict, List, Optional, Type, TypeVar

from src.models.base import Base
from src.persistence.repository import Repository
from utils.populate import populate_db

# Define a generic type for repository models
T = TypeVar("T", bound=Base)


class MemoryRepository(Repository):
    """In-memory repository for storing data temporarily."""

    def __init__(self) -> None:
        """
        Initialize the MemoryRepository.

        The constructor calls the reload method to populate the repository with initial data.
        """
        self.data: Dict[str, List[Base]] = {
            "country": [],
            "user": [],
            "amenity": [],
            "city": [],
            "review": [],
            "place": [],
            "placeamenity": [],
        }
        self.reload()

    def get_all(self, model_name: str) -> List[Base]:
        """Retrieve all objects of a specified model."""
        return self.data.get(model_name, [])

    def get(self, model_name: str, obj_id: str) -> Optional[Base]:
        """Retrieve an object by its ID."""
        return next((obj for obj in self.get_all(model_name) if obj.id == obj_id), None)

    def reload(self) -> None:
        """Populate the repository with initial data."""
        populate_db(self)

    def save(self, obj: Base) -> Base:
        """Save an object to the repository."""
        model_name = obj.__class__.__name__.lower()
        if model_name not in self.data:
            self.data[model_name] = []

        if obj not in self.data[model_name]:
            self.data[model_name].append(obj)

        return obj

    def update(self, obj: Base) -> Optional[Base]:
        """Update an existing object in the repository."""
        model_name = obj.__class__.__name__.lower()
        objects = self.data.get(model_name, [])

        for i, existing_obj in enumerate(objects):
            if existing_obj.id == obj.id:
                obj.updated_at = datetime.now()
                objects[i] = obj
                return obj

        return None

    def delete(self, obj: Base) -> bool:
        """Delete an object from the repository."""
        model_name = obj.__class__.__name__.lower()
        objects = self.data.get(model_name, [])

        if obj in objects:
            objects.remove(obj)
            return True

        return False
