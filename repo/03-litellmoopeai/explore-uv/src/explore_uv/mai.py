import os
import nest_asyncio
from agents import Agent, Runner, function_tool
from agents.extensions.models.litellm_model import LitellmModel

nest_asyncio.apply()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY is None:
    raise ValueError("Please set the GEMINI_API_KEY environment variable.")

MODEL = 'gemini-2.0-flash-lite'

@function_tool
def get_weather(city: str) -> str:
    print(f"[debug] getting weather for {city}")
    return f"The weather in {city} is sunny."

agent = Agent(
    name="Assistant",
    instructions="You only respond in haikus.",
    model=LitellmModel(model=MODEL, api_key=GEMINI_API_KEY),
)

result = Runner.run_sync(agent, "What's the weather in Tokyo?")
print(result.final_output)
