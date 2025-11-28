import os
from openai import OpenAI

DEFAULT_BASE_URL = "https://api.aimlapi.com/v1"

class SimpleAI:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("AIML_API_KEY")
        if not self.api_key:
            raise RuntimeError("Missing AIML_API_KEY")

        base_url = os.getenv("AIML_API_BASE_URL", DEFAULT_BASE_URL)

        self.client = OpenAI(api_key=self.api_key, base_url=base_url)

        self.system_prompt = "You are a simple helpful chatbot."
        self.conversations = {}

    def reset_conversation(self, user_id):
        """Clear chat history for one user."""
        if user_id in self.conversations:
            del self.conversations[user_id]

    def add_user_message(self, user_id, text):
        """Store user's message in history."""
        if not text:
            return
        if user_id not in self.conversations:
            self.conversations[user_id] = []
        self.conversations[user_id].append({"role": "user", "content": text})

    def get_messages(self, user_id):
        """Return full message list with system prompt."""
        history = self.conversations.get(user_id, [])
        messages = [{"role": "system", "content": self.system_prompt}] + history
        return messages

    def get_response(self, user_id):
        """Call the AI model and return the answer text."""
        messages = self.get_messages(user_id)
        try:
            completion = self.client.chat.completions.create(model="gpt-4o-mini",messages=messages,max_tokens=200,temperature=0.7,)
            answer = completion.choices[0].message.content
            if user_id not in self.conversations:
                self.conversations[user_id] = []
            self.conversations[user_id].append({"role": "assistant", "content": answer})
            return answer
        except Exception as e:
            return "AI error: " + str(e)
