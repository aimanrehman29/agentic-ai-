import asyncio
import os
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from dotenv import load_dotenv

load_dotenv()

client = AsyncOpenAI(
    api_key= os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

set_tracing_disabled(disabled=True)

async def main():
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=OpenAIChatCompletionsModel(model="deepseek/deepseek-r1-0528:free", openai_client=client),
    )

    result = await Runner.run(
        agent,
        "Tell me about what is programming.",
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())




