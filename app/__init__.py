from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from config import config_by_name  # Ensure this file exists and is correct
from services.caching import init_cache

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)  # Create Flask app instance

    # Get the environment setting (default to 'development' if not set)
    env = os.getenv('FLASK_ENV', 'development')

    # Ensure the environment is valid and set the config
    if env not in config_by_name:
        raise ValueError(f"Invalid FLASK_ENV: {env}. Must be one of {list(config_by_name.keys())}.")

    app.config.from_object(config_by_name[env])  # Load the corresponding configuration

    # Add cache configuration (e.g., SimpleCache for local testing)
    app.config['CACHE_TYPE'] = 'SimpleCache'
    app.config['CACHE_DEFAULT_TIMEOUT'] = 300  # Default timeout for cache items

    # Initialize Flask extensions (e.g., SQLAlchemy)
    db.init_app(app)

    # Initialize cache
    init_cache(app)

    from app.view import view  # Ensure routes.py exists and contains your routes
    app.register_blueprint(view)

    return app
