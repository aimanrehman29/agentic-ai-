from litellm import completion
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

def gemini():
    response = completion(
        model="gemini-2.0-flash-lite",
        messages=[{"role": "user", "content": "Hello, how are you?"}]
    )
    print("Gemini 2.0 Response:")
    print(response)

# def gemini2():
#     response = completion(
#         model="gemini/gemini-2.0-flash-exp",
#         messages=[{"role": "user", "content": "Hello, how are you?"}]
#     )
#     print("Gemini 2.0 Response:")
#     print(response["choices"][0]["message"]["content"])

if __name__ == "__main__":
    gemini()
    # gemini2()