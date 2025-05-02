import requests
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Retrieve API key from the .env file
API_KEY = os.getenv('OPENWEATHER_API_KEY')
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"


def get_weather_data(city):
    # Properly format the URL
    url = f"{BASE_URL}appid={API_KEY}&q={city}&units=metric"

    # Make the API request
    response = requests.get(url)

    if response.status_code == 200:  # Successful API call
        data = response.json()
        return {  # Return a dictionary of required weather data
            'name': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
    else:  # Handle errors, e.g., invalid city name
        return None

