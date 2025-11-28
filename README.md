# python2project
## python2project
# Weather & AI Assistant Telegram Bot
# Description

This project is a Telegram bot that combines real-time weather information for Barcelona and AI chat assistant powered by AIML API (OpenAI-compatible).

What problem it solves

Lets users quickly check the current weather in Barcelona using OpenWeatherMap.

Provides a built-in conversational AI for answering general questions.

Offers an easy and friendly interface using Telegram inline buttons.

# Main features

/start menu with clickable inline buttons.

Real-time weather based on GPS coordinates.

AI chat mode with memory per-user.


# Screenshots

<img width="1189" height="952" alt="image" src="https://github.com/user-attachments/assets/40de38a0-0618-48fa-bd42-d807abe4e08c" />

<img width="824" height="306" alt="image" src="https://github.com/user-attachments/assets/8e16a3fe-8973-439d-ac4d-4efe5b55e175" />

<img width="764" height="283" alt="image" src="https://github.com/user-attachments/assets/e1f77661-af1c-42e4-8009-688754d4d637" />

# Installation

1. Clone the repository
git clone https://github.com/AleshkaPopovich/python2project.git
cd python2project

2. Preferably activate a virtual environment in order for less complication to appear later on

python -m venv .venv
source .venv/bin/activate   # macOS / Linux
# or
.\.venv\Scripts\activate    # Windows

3. Install dependencies
pip install -r requirements.txt

4. Make sure you have your own token
    (as it is not being run externally)

# Usage
1. Make sure virtual machine is activated

2. Run the bot

    python main.py

3. Open telegram and find bot by its username
    type /start

4. You will see:
    Buttons for cities: Barcelona, Madrid, Valencia, Seville
    A button AI chat

5. Weather mode
    Tap a city → the bot shows:
    Description
    Temperature
    Feels like
    Humidity
    You can tap other cities without restarting the bot.

6. AI chat mode
    Tap “AI chat”
    The bot will switch to AI mode and will tell you to send messages
    Your messages are sent to the AI model(Chatgpt hehe) and you get a reply
    Type /stopai to exit the AI mode


# TODO
    Save conversation history to a file, instead of only in memory

    Add more cities dynamically via user input

    Deploy the bot to an online server

    Add logging in I guess

# Project Structure
    python2project/
├── .venv/                # Virtual environment (ignored in git)
├── __pycache__/          # cahce files from python( ignored as well)
├── .gitignore            # ignored files (includes .env, .venv, __pychache__)
├── .env                  # Environment variables (NOT committed)
├── README.md             # This file
├── requirements.txt      # Python dependencies
├── main.py               # file which is run to start the bot
├── config.py             # Loads env variables, defines CITIES and data structures
├── ai.py                 # AI class basically
├── telegram_bot.py       # WeatherBot class: Telegram bot, handlers, AI chat mode
└──weather_service.py    # WeatherService class which basically calls calls OpenWeather API


# Team Members
    Pau
    Artem
    Github(Artem): @AleshkaPopovich
    Email(Artem) : artemganeev07@gmail.com







