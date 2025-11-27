from config import OWM_API_KEY, CITIES, BOT_TOKEN
from weather_service import WeatherService
from telegram_bot import WeatherBot

def main():
    weather_service = WeatherService(OWM_API_KEY, CITIES)

    bot = WeatherBot(BOT_TOKEN, weather_service, CITIES)

    bot.run()

if __name__ == "__main__":
    main()
