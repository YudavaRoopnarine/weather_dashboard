from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


class Config:
    """Base configuration with default settings."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_password')
    # SECRET_KEY = os.getenv('DATABASE_PASSWORD',
    #                        'default_password')  #  maintain the integrity of sessions and prevent tampering
    DEBUG = True  # enable or disable debug mode.
    TESTING = False  # Disables certain features (like error catching) to make testing easier.
    SQLALCHEMY_TRACK_MODIFICATIONS = False  #  track changes to objects and emit signals False improves performance
    CACHE_TYPE = 'SimpleCache'  # Specifies the caching backend used by Flask-Caching Examples: 'SimpleCache',
    # 'RedisCache', or 'NullCache'.
    CACHE_DEFAULT_TIMEOUT = 300  # 5 minutes


class DevelopmentConfig(Config):  # Extends the Config class with settings specific to development.
    """Development environment settings."""
    DEBUG = True  # Enables detailed error messages and hot reloading when code changes.
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URI', 'sqlite:///dev_db.sqlite')
    # SQLALCHEMY_DATABASE_URI = os.getenv(
    #     'DEV_DATABASE_URI',
    #     'postgresql://username:password@localhost/weather_dashboard'
    #
    # )  # points to a local database
    CACHE_TYPE = 'NullCache'  # Disables caching during development changes are immediate without worrying on stale data


class TestingConfig(Config):  # Extends the Config class with settings for running automated tests.
    """Testing environment settings."""
    TESTING = True  # Enables testing mode, which turns off error catching and simplifies debugging during tests
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI', 'sqlite:///test_db.sqlite')
    # SQLALCHEMY_DATABASE_URI = os.getenv(
    #     'TEST_DATABASE_URI',
    #     'sqlite:///test_db.sqlite'
    # )  # Points to a lightweight in-memory database
    CACHE_TYPE = 'NullCache'  # Disables caching to ensure predictable results and avoid stale data in tests.
    WTF_CSRF_ENABLED = False  # Disables CSRF protection to simplify form testing. Not needed in production.


class ProductionConfig(Config):  # Extends the Config class with secure and performance-optimized settings.
    """Production environment settings."""
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URI', 'sqlite:///prod_db.sqlite')
    # SQLALCHEMY_DATABASE_URI = os.getenv(
    #     'PROD_DATABASE_URI',
    #     'postgresql://user:Smackthat25!@prod-host/prod_db'
    # )  # Points to the production database. This is often hosted on a managed cloud database service
    CACHE_TYPE = 'RedisCache'  # Uses Redis as the caching backend for better performance and scalability.
    CACHE_REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    # CACHE_REDIS_URL = os.getenv('REDIS_URL',
    #                             'redis://localhost:6379/0')  # The connection string for the Redis cache service.
    DEBUG = False
    LOGGING_LEVEL = 'WARNING'


config_by_name = {  # Maps configuration names (development, testing, production) to their corresponding classes.
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}


# class Config:
#     CACHE_TYPE = 'SimpleCache'  # In-memory cache
#     CACHE_DEFAULT_TIMEOUT = 300  # 5 minutes
#
#
# class DevelopmentConfig(Config):
#     CACHE_TYPE = 'NullCache'  # No caching in development
#
#
# class ProductionConfig(Config):
#     CACHE_TYPE = 'RedisCache'  # Use Redis for caching
#     CACHE_REDIS_URL = 'redis://localhost:6379/0'

# Why Have Multiple Configurations?
# Flexibility Across Environments:
# Development: Prioritizes ease of debugging and testing changes locally.
# Testing: Optimized for fast, reproducible tests in isolation.
# Production: Focuses on security, performance, and scalability.
# Security and Separation:
# Prevents sensitive production data (e.g., API keys) from being exposed in development or testing environments.
# Ensures that only secure and optimized settings are used in production.
