# AI Agents Setup with OpenRouter and Google Gemini

This project shows how to make AI agents in three simple ways using the OpenAI Agents SDK and APIs like OpenRouter and Google Gemini:

- **Agent Level**  
- **Run Level**  
- **Global Level**  

---

## What Are These 3 Agents?

We made 3 agents. Each uses one of these ways to set up the AI model and client.

### 1. Agent Level (Deepseek model)

- Here, the AI model and client are set inside the agent itself.  
- This means every agent has its own special setup.  
- Good when you want different agents to use different AI models.  
- This agent uses the **Deepseek** model.

### 2. Run Level (Deepseek model)

- The agent is made without AI setup.  
- The AI model and client are given **only when you run the agent**.  
- This is helpful if you want to change the AI model or client anytime without making a new agent.  
- This also uses the **Deepseek** model.

### 3. Global Level (Gemini model)

- You set the AI model and client **once for all agents**.  
- Every agent will use this setup by default.  
- This is the easiest way if most agents use the same AI.  
- This agent uses the **Google Gemini 2.0** model.

---

## What’s the Difference?

| Setup Level  | When You Set AI Model/Client | How It Works               | Best When...                         |
|--------------|------------------------------|----------------------------|------------------------------------|
| Agent Level  | While creating the agent      | Each agent has its own AI   | You want different agents with different AI  |
| Run Level    | When running the agent        | Change AI on the fly        | You want to switch AI models anytime         |
| Global Level | Once for all agents globally  | All agents use same AI      | Most agents use same AI setup                 |

---

## Which One Should You Use?

- Use **Agent Level** if you want many agents with different AI models.  
- Use **Run Level** if you want to change AI models easily without making new agents.  
- Use **Global Level** if you want simple setup and most agents use the same AI.

---

## Models We Used

- **Deepseek** for Agent and Run level examples.  
- **Google Gemini 2.0** for Global level example.

---

Feel free to explore the code and see how these agents work!
