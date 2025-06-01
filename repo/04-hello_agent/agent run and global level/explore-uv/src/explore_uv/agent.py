import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
import os
from dotenv import load_dotenv

load_dotenv()

client = AsyncOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("BASE_URL"),
)

set_tracing_disabled(disabled=True)

async def chat():
    agent = Agent(
        name="Assistant",
        instructions=
        (
            "You are a helpful assistant that only answers questions related to programming. "
            "If the question is outside programming, politely respond: "
            "'Sorry, I only answer programming related questions.'"
        ),
        model=OpenAIChatCompletionsModel(model="deepseek/deepseek-r1-0528:free", openai_client=client),
    )

    print("Chatbot is ready! Type your message (or 'exit' to quit):")
    while True:
        user_input = input("> ")
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        
        result = await Runner.run(agent, user_input)
        print(result.final_output)

if __name__ == "__main__":
    asyncio.run(chat())


# python -m src.explore_uv.main
