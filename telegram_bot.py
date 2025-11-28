import re
import telebot
from telebot import types
from config import BOT_TOKEN, CITIES, CITY_ORDER
from weather_service import WeatherService
from ai import SimpleAI

def city_name_generator(cities):
    for name in cities:
        yield name

def is_valid_user_text(text):
    return bool(re.search(r"\S", text))

class WeatherBot:
    def __init__(self, token, weather_service, cities, ai_client=None):
        self.bot = telebot.TeleBot(token)
        self.weather_service = weather_service
        self.cities = cities
        self.ai_client = ai_client  
        self.ai_chat_users = set()
        print("bot started")
        self.register_handlers()

    def register_handlers(self):

        @self.bot.message_handler(commands=['start'])
        def start_message(message):
            chat_id = message.chat.id
            keyboard = types.InlineKeyboardMarkup()

            for city in city_name_generator(CITY_ORDER):
                button = types.InlineKeyboardButton(city, callback_data=city)
                keyboard.add(button)
            ai_button = types.InlineKeyboardButton("AI chat", callback_data="AI_CHAT")
            keyboard.add(ai_button)

            self.bot.send_message(chat_id, "Choose a city or start AI:", reply_markup=keyboard)

        @self.bot.callback_query_handler(func=lambda call: True)
        def handle_city_or_ai(call):
            data = call.data
            chat_id = call.message.chat.id
            user_id = call.from_user.id

            if data == "AI_CHAT":
                if self.ai_client is None:
                    self.bot.edit_message_text(chat_id=chat_id,message_id=call.message.message_id,text="AI is not available:(.")
                    return
                self.ai_chat_users.add(user_id)
                self.ai_client.reset_conversation(user_id)
                self.bot.edit_message_text(chat_id=chat_id,message_id=call.message.message_id,text="Send me messages:).\nType /stopai to stop AI.")
                return

            city_name = data
            weather_text = self.weather_service.get_weather(city_name)

            keyboard = types.InlineKeyboardMarkup()
            for city in city_name_generator(CITY_ORDER):
                button = types.InlineKeyboardButton(city, callback_data=city)
                keyboard.add(button)
            ai_button = types.InlineKeyboardButton("AI chat", callback_data="AI_CHAT")
            keyboard.add(ai_button)

            new_text = "Weather in "+city_name+":\n"+weather_text+"\n\nChoose another city or AI chat:"

            self.bot.edit_message_text(chat_id=chat_id,message_id=call.message.message_id,text=new_text,reply_markup=keyboard)

        @self.bot.message_handler(content_types=['text'])
        def handle_text(message):
            user_id = message.from_user.id
            chat_id = message.chat.id
            text = (message.text or "").strip()

            if not is_valid_user_text(text):
                self.bot.send_message(chat_id, "Please send some text, not an empty message.")
                return

            if text.lower() in ("/stopai", "stop ai"):
                if user_id in self.ai_chat_users:
                    self.ai_chat_users.remove(user_id)
                    self.bot.send_message(chat_id, "AI chat stopped. Use /start to go back.")
                return

            if user_id not in self.ai_chat_users:
                return

            if self.ai_client is None:
                self.bot.send_message(chat_id, "AI is not available.")
                return

            self.ai_client.add_user_message(user_id, text)
            answer = self.ai_client.get_response(user_id)
            self.bot.send_message(chat_id, answer)

    def run(self):
        self.bot.infinity_polling()
