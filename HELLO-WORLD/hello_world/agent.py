from google.adk import Agent
# Use relative import for your tools
from .tools import get_current_time, calculate_sum, say_hello

# This 'root_agent' variable is what the ADK is searching for.
root_agent = Agent(
    name="hello_world", # Matches agent_name in adk.config.json
    model = "gemini-2.0-flash",
    global_instruction="You are a simple conversational bot for hello world agent.",
    instruction="Keep the conversation short, limit of 100 words max in response.",
    tools=[get_current_time, calculate_sum, say_hello]
)


def create_agent():
    return root_agent