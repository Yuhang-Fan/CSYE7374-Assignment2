import math
import datetime
import pytz
import re

def calculator_tool(expression: str) -> str:
    """
    Evaluate math expressions with support for sin, cos, log, etc., using degrees.
    """
    try:
        expression = re.sub(r'(?<![a-zA-Z])sin\((\d+(\.\d+)?)\)', r'sin(radians(\1))', expression)
        expression = re.sub(r'(?<![a-zA-Z])cos\((\d+(\.\d+)?)\)', r'cos(radians(\1))', expression)
        expression = re.sub(r'(?<![a-zA-Z])tan\((\d+(\.\d+)?)\)', r'tan(radians(\1))', expression)

        allowed_funcs = {
            k: getattr(math, k) for k in [
                "sin", "cos", "tan", "log", "sqrt", "radians", "degrees",
                "pi", "e", "log10", "log2", "exp", "fabs", "factorial", "pow"
            ]
        }
        result = eval(expression, {"__builtins__": None}, allowed_funcs)
        return f"Result: {result}"
    except Exception as e:
        return f"Error in calculation: {str(e)}"

def get_current_time(timezone: str = "UTC") -> str:
    """
    Return the current time in the given timezone.

    Args:
        timezone: Timezone string like "UTC", "Asia/Tokyo", "US/Eastern"

    Returns:
        Formatted time string with timezone info
    """
    try:
        tz = pytz.timezone(timezone)
        now = datetime.datetime.now(tz)
        return now.strftime(f"%Y-%m-%d %H:%M:%S {timezone}")
    except Exception as e:
        return f"Invalid timezone: {str(e)}"

def web_search(query: str, num_results: int = 3) -> str:
    """
    Placeholder search function. Enhanced web search removed.
    """
    return "Web search is currently disabled in this bot version."
