from typing import List, Optional, Type, TypeVar, Dict
from src.models.base import Base
from src.persistence.repository import Repository

# Define a generic type variable for repository models
T = TypeVar("T", bound=Base)


class DBRepository(Repository):
    """Database repository using SQLAlchemy."""

    def __init__(self, database_url: str) -> None:
        """Initialize the repository with the given database URL.

        Args:
            database_url (str): The database connection URL.
        """
        self.engine = create_engine(database_url)
        Base.metadata.bind = self.engine
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.reload()

    def get_all(self, model_name: str) -> List[Base]:
        """Retrieve all objects of a specified model from the database.

        Args:
            model_name (str): The name of the model to retrieve objects for.

        Returns:
            List[Base]: A list of objects of the specified model.
        """
        model_class = self._get_model_class(model_name)
        if model_class:
            return self.session.query(model_class).all()
        return []

    def get(self, model_name: str, obj_id: str) -> Optional[Base]:
        """Retrieve a single object by its ID from the database.

        Args:
            model_name (str): The name of the model to retrieve the object for.
            obj_id (str): The ID of the object to retrieve.

        Returns:
            Optional[Base]: The object if found, else None.
        """
        model_class = self._get_model_class(model_name)
        if model_class:
            return self.session.query(model_class).filter_by(id=obj_id).first()
        return None

    def save(self, obj: Base) -> Base:
        """Save an object to the database.

        Args:
            obj (Base): The object to save.

        Returns:
            Base: The saved object.
        """
        self.session.add(obj)
        self.session.commit()
        return obj

    def update(self, obj: Base) -> Optional[Base]:
        """Update an existing object in the database.

        Args:
            obj (Base): The object to update.

        Returns:
            Optional[Base]: The updated object if found and updated, else None.
        """
        existing_obj = self.get(obj.__class__.__name__.lower(), obj.id)
        if existing_obj:
            for key, value in obj.to_dict().items():
                setattr(existing_obj, key, value)
            self.session.commit()
            return existing_obj
        return None

    def delete(self, obj: Base) -> bool:
        """Delete an object from the database.

        Args:
            obj (Base): The object to delete.

        Returns:
            bool: True if the object was deleted, else False.
        """
        existing_obj = self.get(obj.__class__.__name__.lower(), obj.id)
        if existing_obj:
            self.session.delete(existing_obj)
            self.session.commit()
            return True
        return False

    def reload(self) -> None:
        """Reload the database schema and data.

        This method can be used to initialize the database schema or seed initial data.
        """
        Base.metadata.create_all(self.engine)

    def _get_model_class(self, model_name: str) -> Optional[Type[Base]]:
        """Retrieve the model class based on the model name.

        Args:
            model_name (str): The name of the model to retrieve.

        Returns:
            Optional[Type[Base]]: The model class if found, else None.
        """
        from src.models import Country, User, Amenity, City, Place, Review, PlaceAmenity

        model_classes: Dict[str, Type[Base]] = {
            "country": Country,
            "user": User,
            "amenity": Amenity,
            "city": City,
            "place": Place,
            "review": Review,
            "placeamenity": PlaceAmenity,
        }

        return model_classes.get(model_name.lower())
