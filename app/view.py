from flask import render_template, request, jsonify, Blueprint, Flask
from .services.weather_api import get_weather_data
from .services.caching import cache_data, get_cached_data

import requests
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Retrieve API key from the .env file
API_KEY = os.getenv('OPENWEATHER_API_KEY')
url = "https://api.openweathermap.org/data/2.5/weather?"

view = Blueprint('view', __name__)


# Home route
@view.route('/')
def index():
    return render_template('index.html')


@view.route('/weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')  # Retrieve city input from the form
    # weather = cache_data(city, get_weather_data(city))  # Fetch weather data using helper function

    # Check if cached data exists
    cached_weather = get_cached_data(city)
    if cached_weather:
        return jsonify({"source": "cache", "data": cached_weather})

    response = requests.get(url).json()
    cache_data(city, response, timeout=300)

    # return render_template('index.html', weather=weather)
    return jsonify({"source": "API", "data": response})

