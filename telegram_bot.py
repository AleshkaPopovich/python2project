import telebot
from telebot import types
from config import BOT_TOKEN, CITIES
from weather_service import WeatherService

class WeatherBot:
    def __init__(self, token, weather_service, cities):
        self.bot = telebot.TeleBot(token)
        self.weather_service = weather_service
        self.cities = cities

        print("bot started")

        self.register_handlers()

    def callback_all(self, call):
        return True

    def register_handlers(self):
        @self.bot.message_handler(commands=['start'])
        def start_message(message):
            chat_id = message.chat.id

            keyboard = types.InlineKeyboardMarkup()
            for city in self.cities:
                button = types.InlineKeyboardButton(city, callback_data=city)
                keyboard.add(button)

            self.bot.send_message(chat_id, "Choose a city:", reply_markup=keyboard)

        @self.bot.callback_query_handler(func=self.callback_all)
        def handle_city_choice(call):
            city_name = call.data

            weather_text = self.weather_service.get_weather(city_name)

            keyboard = types.InlineKeyboardMarkup()
            for city in self.cities:
                button = types.InlineKeyboardButton(city, callback_data=city)
                keyboard.add(button)

            new_text = "Weather in " + city_name + ":\n" + weather_text + "\n\nChoose another city:"

            self.bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=new_text,
                reply_markup=keyboard
            )

    # run bot forever
    def run(self):
        self.bot.infinity_polling()
