# Async Programming Chatbot with OpenRouter Deepseek Model

## Overview

This project is an asynchronous chatbot built in Python that connects to the OpenRouter API to use the `deepseek/deepseek-r1-0528:free` language model. The chatbot is designed to answer programming-related questions in a conversational way.

The bot restricts its responses to programming topics and politely declines to answer questions outside this domain.

Additionally, this project leverages **Universal Viewer (UV)** technology for enhanced interaction capabilities and efficient management of asynchronous tasks.

---
## Features

- Asynchronous communication with the OpenRouter LLM model using Python's `asyncio`.
- Modular design separating agent logic and user interface.
- Environment variable support via `.env` for secure API key management.
- Domain-specific chatbot instructions for focused, relevant responses.
- Command-line interactive chatbot loop.

---

## Setup Instructions

### Prerequisites

- Python 3.8 or above
- An API key from [OpenRouter](https://openrouter.ai/)
- Virtual environment (recommended)
