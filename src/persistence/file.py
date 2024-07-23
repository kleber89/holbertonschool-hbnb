""" 
    Lst
"""
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Type, TypeVar

from src.models.base import Base
from src.persistence.repository import Repository
from utils.constants import FILE_STORAGE_FILENAME

# Define a generic type for repository models
T = TypeVar("T", bound=Base)


class FileRepository(Repository):
    """File-based repository for storing and managing data."""

    def __init__(self, filename: str = FILE_STORAGE_FILENAME) -> None:
        """
        Initialize the FileRepository.

        :param filename: Path to the file for storing data.
        """
        self.filename = filename
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

    def _save_to_file(self) -> None:
        """Helper method to save current data to the file."""
        serialized_data = {
            model_name: [obj.to_dict() for obj in objects]
            for model_name, objects in self.data.items()
        }
        with open(self.filename, "w") as file:
            json.dump(serialized_data, file, indent=4)

    def get_all(self, model_name: str) -> List[Base]:
        """Retrieve all objects of a given model."""
        return self.data.get(model_name, [])

    def get(self, model_name: str, obj_id: str) -> Optional[Base]:
        """Retrieve an object by its ID."""
        for obj in self.get_all(model_name):
            if obj.id == obj_id:
                return obj
        return None

    def reload(self) -> None:
        """Load data from the file."""
        if not os.path.exists(self.filename):
            self._initialize_default_data()
            return

        with open(self.filename, "r") as file:
            file_data = json.load(file)

        model_classes = self._get_model_classes()

        for model_name, items in file_data.items():
            model_class = model_classes.get(model_name)
            if model_class:
                for item in items:
                    instance = model_class(**item)
                    if "created_at" in item:
                        instance.created_at = datetime.fromisoformat(item["created_at"])
                    if "updated_at" in item:
                        instance.updated_at = datetime.fromisoformat(item["updated_at"])
                    self.save(instance, save_to_file=False)

    def _initialize_default_data(self) -> None:
        """Initialize repository with default data."""
        from src.models.country import Country

        self.data["country"] = [Country(name="Uruguay", code="UY")]
        self._save_to_file()

    def _get_model_classes(self) -> Dict[str, Type[Base]]:
        """Return a dictionary of model names to classes."""
        from src.models.amenity import Amenity
        from src.models.city import City
        from src.models.country import Country
        from src.models.place import Place
        from src.models.review import Review
        from src.models.user import User
        from src.models.placeamenity import PlaceAmenity

        return {
            "amenity": Amenity,
            "city": City,
            "country": Country,
            "place": Place,
            "placeamenity": PlaceAmenity,
            "review": Review,
            "user": User,
        }

    def save(self, data: Base, save_to_file: bool = True) -> None:
        """Save an object to the repository."""
        model_name = data.__class__.__name__.lower()
        if model_name not in self.data:
            self.data[model_name] = []
        self.data[model_name].append(data)
        if save_to_file:
            self._save_to_file()

    def update(self, obj: Base) -> Optional[Base]:
        """Update an existing object in the repository."""
        model_name = obj.__class__.__name__.lower()
        for i, existing_obj in enumerate(self.data.get(model_name, [])):
            if existing_obj.id == obj.id:
                obj.updated_at = datetime.now()
                self.data[model_name][i] = obj
                self._save_to_file()
                return obj
        return None

    def delete(self, obj: Base) -> bool:
        """Delete an object from the repository."""
        model_name = obj.__class__.__name__.lower()
        if obj in self.data.get(model_name, []):
            self.data[model_name].remove(obj)
            self._save_to_file()
            return True
        return False
