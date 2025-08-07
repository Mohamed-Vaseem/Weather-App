import requests
import os

API_KEY = os.getenv("API_KEY")
city = input("Enter your city:")  # or any input

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"\nWeather in {data['name']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Condition: {data['weather'][0]['description'].capitalize()}")
    else:
        print("\nCity not found. Try again!")

get_weather(city, API_KEY)
