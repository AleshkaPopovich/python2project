from config import OWM_API_KEY, CITIES, BOT_TOKEN, AIML_API_KEY
from weather_service import WeatherService
from telegram_bot import WeatherBot
from ai import SimpleAI

def main():
    weather_service = WeatherService(OWM_API_KEY, CITIES)
    ai_client = None
    try:
        ai_client = SimpleAI(AIML_API_KEY)
    except RuntimeError:
        print("Bot will still run without AI, due to AI disabling (missing AIML_API_KEY).")
    bot = WeatherBot(BOT_TOKEN, weather_service, CITIES, ai_client)
    bot.run()

if __name__ == "__main__":
    main()

