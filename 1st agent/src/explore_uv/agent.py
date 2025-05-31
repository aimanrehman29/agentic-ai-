from openai import AsyncOpenAI

class OpenAIChatCompletionsModel:
    def __init__(self, model, openai_client):
        self.model = model
        self.client = openai_client

    async def chat(self, prompt):
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content


class Agent:
    def __init__(self, name, instructions, model):
        self.name = name
        self.instructions = instructions
        self.model = model

    async def run(self, prompt):
        # Combine instructions with user prompt
        full_prompt = f"{self.instructions}\n\n{prompt}"
        return await self.model.chat(full_prompt)


class Runner:
    @staticmethod
    async def run(agent, prompt):
        output = await agent.run(prompt)
        class Result:
            final_output = output
        return Result()

def set_tracing_disabled(disabled):
    # No tracing implementation needed here
    pass
