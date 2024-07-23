""" 
    Lts
"""

import pickle
from typing import Dict, List, Optional, Type, TypeVar

from src.models.base import Base
from src.persistence.repository import Repository
from utils.constants import PICKLE_STORAGE_FILENAME

# Define a generic type for repository models
T = TypeVar("T", bound=Base)


class PickleRepository(Repository):
    """Repository that persists data using pickle."""

    def __init__(self) -> None:
        """
        Initialize the PickleRepository.

        The constructor calls the reload method to load data from the pickle file.
        """
        self.filename = PICKLE_STORAGE_FILENAME
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
        """Save the current state of the repository to a pickle file."""
        with open(self.filename, "wb") as file:
            pickle.dump(self.data, file)

    def get_all(self, model_name: str) -> List[Base]:
        """Retrieve all objects of a specified model."""
        return self.data.get(model_name, [])

    def get(self, model_name: str, obj_id: str) -> Optional[Base]:
        """Retrieve an object by its ID."""
        return next((obj for obj in self.get_all(model_name) if obj.id == obj_id), None)

    def reload(self) -> None:
        """Load data from the pickle file into the repository."""
        try:
            with open(self.filename, "rb") as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            from src.models.country import Country

            # Load default data if the file does not exist
            self.data["country"] = [Country("Uruguay", "UY")]
            self._save_to_file()

    def save(self, obj: Base, save_to_file: bool = True) -> Base:
        """Save an object to the repository."""
        model_name = obj.__class__.__name__.lower()
        if model_name not in self.data:
            self.data[model_name] = []

        if obj not in self.data[model_name]:
            self.data[model_name].append(obj)

        if save_to_file:
            self._save_to_file()

        return obj

    def update(self, obj: Base) -> Optional[Base]:
        """Update an existing object in the repository."""
        model_name = obj.__class__.__name__.lower()
        objects = self.data.get(model_name, [])

        for i, existing_obj in enumerate(objects):
            if existing_obj.id == obj.id:
                obj.updated_at = datetime.now()
                objects[i] = obj
                self._save_to_file()
                return obj

        return None

    def delete(self, obj: Base) -> bool:
        """Delete an object from the repository."""
        model_name = obj.__class__.__name__.lower()
        objects = self.data.get(model_name, [])

        for i, existing_obj in enumerate(objects):
            if existing_obj.id == obj.id:
                del objects[i]
                self._save_to_file()
                return True

        return False
