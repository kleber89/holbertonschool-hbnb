"""Abstract base class for all models"""

from datetime import datetime
from typing import Any, Optional
import uuid
from abc import ABC, abstractmethod


class Base(ABC):
    """
    Base for all models
    """

    id: str
    created_at: datetime
    updated_at: datetime

    def __init__(
        self,
        id: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        **kwargs,
    ) -> None:
        """
        Base class constructor.
        If kwargs are provided, set them as attributes.
        """
        self.id = str(id or uuid.uuid4())
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

        # Set additional attributes from kwargs
        for key, value in kwargs.items():
            if not hasattr(self, key):
                setattr(self, key, value)

    @classmethod
    def get(cls, id: str) -> Optional[Any]:
        """
        Common method to get a specific object of a class by its id.
        If a class needs a different implementation, it should override this method.
        """
        from src.persistence import repo

        return repo.get(cls.__name__.lower(), id)

    @classmethod
    def get_all(cls) -> list[Any]:
        """
        Common method to get all objects of a class.
        If a class needs a different implementation, it should override this method.
        """
        from src.persistence import repo

        return repo.get_all(cls.__name__.lower())

    @classmethod
    def delete(cls, id: str) -> bool:
        """
        Common method to delete a specific object of a class by its id.
        If a class needs a different implementation, it should override this method.
        """
        from src.persistence import repo

        obj = cls.get(id)
        if not obj:
            return False
        return repo.delete(obj)

    @abstractmethod
    def to_dict(self) -> dict:
        """Returns the dictionary representation of the object"""

    @staticmethod
    @abstractmethod
    def create(data: dict) -> Any:
        """Creates a new object of the class"""

    @staticmethod
    @abstractmethod
    def update(entity_id: str, data: dict) -> Optional[Any]:
        """Updates an object of the class"""
