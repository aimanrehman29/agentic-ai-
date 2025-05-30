# agents.py

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(dotenv_path="src/explore_uv/.env")  # Adjust path to your .env

class Agent:
    def __init__(self, api_key=None, model="gemini-2.0-flash"):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not set.")
        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        self.history = []

    async def ask(self, question):
        self.history.append({"role": "user", "content": question})
        response = await self.client.chat.completions.acreate(
            model=self.model,
            messages=self.history
        )
        answer = response.choices[0].message.content
        self.history.append({"role": "assistant", "content": answer})
        return answer
