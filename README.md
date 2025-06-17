# Agent Development Kit (ADK) || Hello World Agent




<html>
    <h2 align="center">
      <img src="https://raw.githubusercontent.com/google/adk-python/main/assets/agent-development-kit.png" width="256"/>
    </h2>
    <h3 align="center">
      An open-source, code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.
    </h3>
    <h3 align="center">
      Important Links:
      <a href="https://google.github.io/adk-docs/">Docs</a>, 
      <a href="https://github.com/google/adk-web">ADK Web</a>.
    </h3>
</html>


This repository contains a simple **"Hello World"** agent built using the **Google Agent Development Kit (ADK)**. The agent demonstrates basic conversational skills and tool usage through a few predefined Python functions.

---

## 🧠 What is the Agent Development Kit (ADK)?

The **Google Agent Development Kit (ADK)** is a powerful framework for building, deploying, and managing AI agents powered by large language models (LLMs). It provides a structured way to define agent behavior, connect with models like Gemini, and use custom tools.

### 🚀 Key Benefits

- **Simplified Agent Creation**: Focus on what the agent should do, not the AI plumbing.
- **Modular Tool Design**: Write reusable Python functions (called tools).
- **LLM-Driven Reasoning**: The agent decides when and how to use tools.
- **Conversation Flow Management**: Handles tool execution and response generation.
- **Deployment Readiness**: Built with production deployment in mind.

---

## 🧩 How it Works

1. **Define the Agent**: Use the `Agent` class to set its name, model, instructions, and tools.
2. **Create Tools**: Functions like `get_current_time()` or `calculate_sum()` give the agent new capabilities.
3. **LLM + Tool Orchestration**:
   - User input goes to the LLM.
   - LLM reasons whether to call a tool.
   - ADK executes the tool and passes the result back.
   - LLM generates the final response.

---

## 📁 Project Structure

```
hello_world_agent/
├── agent.py          # Main entry point that defines the root agent
├── __init__.py       # Enables agent discovery
└── tools/            # Folder containing the tools module
    └── tools.py      # Custom functions the agent can use

```

---

## 📜 agent.py

```python
from google.adk import Agent
from .tools import get_current_time, calculate_sum, say_hello

root_agent = Agent(
    name="hello_world",
    model="gemini-2.0-flash",
    global_instruction="You are a simple conversational bot for hello world agent.",
    instruction="Keep the conversation short, limit of 100 words max in response.",
    tools=[get_current_time, calculate_sum, say_hello]
)

def create_agent():
    return root_agent
```

---

## 🔧 tools.py

```python
import datetime

def get_current_time():
    """
    Tool Name: get_current_time

    Description:
        Retrieves the current system date and time.

    Usage:
        Use this tool when the user asks for the current time or date.

    Returns:
        A string in the format: "The current date and time is: YYYY-MM-DD HH:MM:SS"

    Example:
        User: What time is it?
        Agent: The current date and time is: 2025-06-17 14:30:45
    """
    now = datetime.datetime.now()
    return f"The current date and time is: {now.strftime('%Y-%m-%d %H:%M:%S')}"

def calculate_sum(num1: float, num2: float):
    """
    Tool Name: calculate_sum

    Description:
        Adds two numeric values and returns the result in a formatted string.

    Usage:
        Use this tool when the user asks for a basic addition operation.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        A string indicating the result of the addition.
        Example: "The sum of 4.0 and 5.0 is 9.0."

    Error Handling:
        If non-numeric input is provided, returns an error message.

    Example:
        User: Add 12 and 8
        Agent: The sum of 12.0 and 8.0 is 20.0.
    """
    try:
        result = num1 + num2
        return f"The sum of {num1} and {num2} is {result}."
    except TypeError:
        return "Error: Please provide valid numbers for calculation."

def say_hello():
    """
    Tool Name: say_hello

    Description:
        Returns a simple friendly greeting message.

    Usage:
        Use this tool when the user greets or expects a hello-type interaction.

    Returns:
        A static greeting string: "Hello from your ADK Agent!"

    Example:
        User: Hi!
        Agent: Hello from your ADK Agent!
    """
    return "Hello from your ADK Agent!"

```

---

## 🛠️ Available Tools

| Tool              | Description                                  |
|-------------------|----------------------------------------------|
| `get_current_time()` | Returns the current date and time.         |
| `calculate_sum(num1, num2)` | Adds two numbers and returns the result. |
| `say_hello()`      | Returns a simple greeting message.          |

---

###  > 📘 **[Importance of Docstring](doc/docstring_adk.md)**

## ⚙️ Setup and Installation

### 1. Clone or Create Project Files

Ensure `agent.py`, `__init__.py`, and `tools.py` exist in a directory.

### 2. Install Google ADK

```bash
pip install google-adk
```

### 3. Authenticate with Google Cloud

```bash
gcloud auth application-default login
```

> This step is required to access models like Gemini via ADK.

---

## 🧪 Running the Agent Locally

### Run via Terminal

```bash
cd path/to/hello_world_agent/
adk run hello_world
```

### Sample Interactions

| User Input                        | Agent Response                                       |
|----------------------------------|------------------------------------------------------|
| `Hello!`                         | Hello from your ADK Agent!                          |
| `What's the current time?`       | The current date and time is: YYYY-MM-DD HH:MM:SS   |
| `Add 10 and 5`                   | The sum of 10.0 and 5.0 is 15.0.                    |
| `Hi, what time is it?`           | Hello from your ADK Agent! The current date is...   |

---

## 🌐 ADK Web (Experimental)

### Run with Web Interface

```bash
adk web hello_world
```

Visit `http://localhost:8080` in your browser to chat with the agent.

---

## ✅ Summary

This Hello World agent provides a minimal but complete starting point for working with the ADK. It highlights how LLMs can be extended through tool usage to handle user requests programmatically.

---

## 📄 License

Licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
