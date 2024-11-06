class Amenity(BaseModel):
    def __init__(self, id, name):
        # ... existing code ...
        self.id = id  # Unique identifier
        self.name = self.validate_name(name)  # Validate name
        # ... existing code ...

    def validate_name(self, name):
        if not name or len(name) > 50:
            raise ValueError("Name is required and must be a maximum of 50 characters.")
        return name

    # ... existing methods ...