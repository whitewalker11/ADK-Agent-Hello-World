# tools.py
import datetime

def get_current_time():
    """
    Returns the current date and time.
    """
    now = datetime.datetime.now()
    return f"The current date and time is: {now.strftime('%Y-%m-%d %H:%M:%S')}"

def calculate_sum(num1: float, num2: float):
    """
    Calculates the sum of two numbers.

    Args:
        num1: The first number.
        num2: The second number.

    Returns:
        The sum of the two numbers.
    """
    try:
        result = num1 + num2
        return f"The sum of {num1} and {num2} is {result}."
    except TypeError:
        return "Error: Please provide valid numbers for calculation."

def say_hello():
    """
    Returns a simple greeting message.
    """
    return "Hello from your ADK Agent!"

# You can add more tools here later!