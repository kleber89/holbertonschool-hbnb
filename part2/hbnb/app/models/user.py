class User(BaseModel):
    existing_emails = set()  # To keep track of existing emails

    def __init__(self, id, first_name, last_name, email, is_admin=False):
        # ... existing code ...
        self.id = id  # Unique identifier
        self.first_name = self.validate_name(first_name, "First name")  # Validate first name
        self.last_name = self.validate_name(last_name, "Last name")  # Validate last name
        self.email = self.validate_email(email)  # Validate email
        self.is_admin = is_admin  # Default is False
        self.check_unique_email(self.email)  # Check for unique email
        # ... existing code ...

    def validate_name(self, name, field_name):
        if not name or len(name) > 50:
            raise ValueError(f"{field_name} is required and must be a maximum of 50 characters.")
        return name

    def validate_email(self, email):
        # Add standard email format validation logic here
        if not email or "@" not in email:  # Simplified validation
            raise ValueError("Email must be valid.")
        return email

    def check_unique_email(self, email):
        if email in User.existing_emails:
            raise ValueError("Email must be unique.")
        User.existing_emails.add(email)  # Add email to the set

    # ... existing methods ...