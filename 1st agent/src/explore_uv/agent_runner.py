import asyncio
from openai import AsyncOpenAI
from .agent import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = ("https://openrouter.ai/api/v1")  
MODEL = "deepseek/deepseek-r1-0528:free"

client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url=BASE_URL
)

set_tracing_disabled(disabled=True)

async def main():
    agent = Agent(
        name="ProgrammingBot",
        instructions=(
            "You are a helpful assistant that only answers questions related to programming. "
            "If the question is outside programming, politely respond: "
            "'Sorry, I only answer programming related questions.'"
        ),
        model=OpenAIChatCompletionsModel(model=MODEL, openai_client=client),
    )

   

    print("Chatbot started! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            print("Goodbye!")
            break

        result = await Runner.run(agent, user_input)
        print("Bot:", result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
