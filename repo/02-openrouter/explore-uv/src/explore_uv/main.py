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

async def main(): 
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=OpenAIChatCompletionsModel(model="deepseek/deepseek-r1-0528:free", openai_client=client),
    )

    result = await Runner.run(
        agent,
        "Tell me about OpenAI Agents SDK .",
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())