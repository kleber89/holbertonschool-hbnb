from datetime import datetime

class User:
    users = []

    def __init__(self, email, first_name, last_name):
        self.id = len(User.users) + 1  # Simple unique identifier
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        # Ensure email is unique
        for user in User.users:
            if user.email == self.email:
                raise ValueError("Email must be unique")
        
        User.users.append(self)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()