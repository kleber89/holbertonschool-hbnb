"""
User class
"""

from src.models.base import Base


class User(Base):
    """User representation"""

    email: str
    first_name: str
    last_name: str

    def __init__(self, email: str, first_name: str, last_name: str, **kwargs):
        """
        Initializes a User instance.
        """
        super().__init__(**kwargs)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self) -> str:
        """
        String representation of the User instance.
        """
        return f"<User {self.id} ({self.email})>"

    def to_dict(self) -> dict:
        """
        Dictionary representation of the User instance.
        """
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(user_data: dict) -> "User":
        """
        Creates a new User instance.
        """
        from src.persistence import repo

        existing_users = User.get_all()
        if any(u.email == user_data["email"] for u in existing_users):
            raise ValueError("User already exists")

        new_user = User(**user_data)
        repo.save(new_user)
        return new_user

    @staticmethod
    def update(user_id: str, data: dict) -> "User | None":
        """
        Updates an existing User instance.
        """
        from src.persistence import repo

        user = User.get(user_id)
        if not user:
            return None

        for key in ["email", "first_name", "last_name"]:
            if key in data:
                setattr(user, key, data[key])

        repo.update(user)
        return user
