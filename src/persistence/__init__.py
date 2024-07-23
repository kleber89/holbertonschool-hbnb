"""This module selects the repository based on the environment variable REPOSITORY_ENV_VAR."""

import os
from src.persistence.repository import Repository
from utils.constants import REPOSITORY_ENV_VAR

# Initialize repository to None
repo: Repository = None

# Determine repository type based on environment variable
repository_type = os.getenv(REPOSITORY_ENV_VAR, "memory").lower()

repository_mapping = {
    "db": "src.persistence.db.DBRepository",
    "file": "src.persistence.file.FileRepository",
    "pickle": "src.persistence.pickled.PickleRepository",
    "memory": "src.persistence.memory.MemoryRepository",
}

# Import and instantiate the appropriate repository class
repository_class = repository_mapping.get(repository_type, repository_mapping["memory"])
module_path, class_name = repository_class.rsplit(".", 1)

module = __import__(module_path, fromlist=[class_name])
repository_class = getattr(module, class_name)

repo = repository_class()

print(f"Using {repo.__class__.__name__} as repository")
