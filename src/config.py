"""
    Aplication export
"""

from abc import ABC
import os

class Config(ABC):
    """
    Base configuration settings.
    This class should not be instantiated directly.
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """
    Development configuration settings.
    This configuration is used when running the application locally
    for development and debugging purposes.
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///hbnb_dev.db")

class TestingConfig(Config):
    """
    Testing configuration settings.
    This configuration is used when running tests.
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

class ProductionConfig(Config):
    """
    Production configuration settings.
    This configuration is used when deploying the application in production.
    """
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/hbnb_prod")
