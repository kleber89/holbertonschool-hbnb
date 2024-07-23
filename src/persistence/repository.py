from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Type, TypeVar, Union

# Define a generic type variable for repository models
T = TypeVar("T", bound="Base")


class Repository(ABC):
    """Abstract base class for a repository pattern."""

    @abstractmethod
    def reload(self) -> None:
        """Reload or initialize the data in the repository."""
        pass

    @abstractmethod
    def get_all(self, model_name: str) -> List[T]:
        """
        Retrieve all objects of a specified model.

        Args:
            model_name (str): The name of the model to retrieve objects for.

        Returns:
            List[T]: A list of objects of the specified model.
        """
        pass

    @abstractmethod
    def get(self, model_name: str, obj_id: str) -> Optional[T]:
        """
        Retrieve a single object by its ID.

        Args:
            model_name (str): The name of the model to retrieve the object for.
            obj_id (str): The ID of the object to retrieve.

        Returns:
            Optional[T]: The object if found, else None.
        """
        pass

    @abstractmethod
    def save(self, obj: T) -> T:
        """
        Save an object to the repository.

        Args:
            obj (T): The object to save.

        Returns:
            T: The saved object.
        """
        pass

    @abstractmethod
    def update(self, obj: T) -> Optional[T]:
        """
        Update an existing object in the repository.

        Args:
            obj (T): The object to update.

        Returns:
            Optional[T]: The updated object if found and updated, else None.
        """
        pass

    @abstractmethod
    def delete(self, obj: T) -> bool:
        """
        Delete an object from the repository.

        Args:
            obj (T): The object to delete.

        Returns:
            bool: True if the object was deleted, else False.
        """
        pass

    def __repr__(self) -> str:
        """Provide a string representation of the repository instance."""
        return f"<{self.__class__.__name__} repository>"
