from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-default-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///weather_dashboard.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # OpenWeatherMap API key
    OPENWEATHERMAP_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY', 'your-default-api-key')
