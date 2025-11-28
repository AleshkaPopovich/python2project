import requests
from config import OWM_API_KEY, CITIES, CITY_NAME_SET

class WeatherService:
    def __init__(self, api_key, cities):
        self.api_key = api_key
        self.cities = cities

    def get_weather(self, city_name):
        if city_name not in CITY_NAME_SET:
            return "City not found"

        coords = (self.cities[city_name]["lat"], self.cities[city_name]["lon"])
        lat, lon = coords

        url = "https://api.openweathermap.org/data/2.5/weather"
        url = url + "?lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + self.api_key + "&units=metric"

        try:
            r = requests.get(url, timeout=10)
            data = r.json()

            main = data["main"]
            weather = data["weather"][0] 

            temp = main["temp"]
            feels_like = main["feels_like"]
            humidity = main["humidity"]
            description = weather["description"]

            text = "Weather: " + str(description) + "\n"
            text = text + "Temperature: " + str(temp) + "°C\n"
            text = text + "Feels like: " + str(feels_like) + "°C\n"
            text = text + "Humidity: " + str(humidity) + "%"

            return text
        except requests.RequestException:
            return "Error getting weather"
        except (ValueError, KeyError):
            return "Error parsing weather data"
