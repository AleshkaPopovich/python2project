import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWM_API_KEY = os.getenv("OWM_API_KEY")


CITIES = {
    "Barcelona": {"lat": 41.3851, "lon": 2.1734},
    "Madrid": {"lat": 40.4168, "lon": -3.7038},
    "Valencia": {"lat": 39.4699, "lon": -0.3763},
    "Seville": {"lat": 37.3891, "lon": -5.9845},
}
