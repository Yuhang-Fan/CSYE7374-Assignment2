# main.py
import openai
import json
from openai import OpenAI
from tools import calculator_tool, get_current_time, web_search
from config import OPENAI_API_KEY, MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

tools_schema = [
    {
        "type": "function",
        "function": {
            "name": "calculator_tool",
            "description": "Perform math calculations",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "Math expression to evaluate"}
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get current time in a timezone",
            "parameters": {
                "type": "object",
                "properties": {
                    "timezone": {"type": "string", "description": "Timezone (e.g., UTC, Asia/Tokyo)"}
                },
                "required": ["timezone"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web for information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "num_results": {"type": "integer", "default": 3}
                },
                "required": ["query"]
            }
        }
    }
]

def call_tool(name, arguments):
    if name == "calculator_tool":
        return calculator_tool(arguments["expression"])
    elif name == "get_current_time":
        return get_current_time(arguments["timezone"])
    elif name == "web_search":
        return web_search(arguments["query"], arguments.get("num_results", 3))
    else:
        return f"Unknown tool: {name}"

def chat_loop():
    messages = [{"role": "system", "content": "You are a helpful assistant that can use tools when needed."}]

    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=tools_schema,
            tool_choice="auto"
        )

        reply = response.choices[0].message

        if reply.tool_calls:
            messages.append({
                "role": "assistant",
                "content": reply.content,
                "tool_calls": reply.tool_calls
            })

            for tool_call in reply.tool_calls:
                func_name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)
                result = call_tool(func_name, args)

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": func_name,
                    "content": result
                })

            second_response = client.chat.completions.create(
                model=MODEL,
                messages=messages
            )
            final_reply = second_response.choices[0].message
            print("Bot:", final_reply.content)
            messages.append({"role": "assistant", "content": final_reply.content})

        else:
            print("Bot:", reply.content)
            messages.append({"role": "assistant", "content": reply.content})


if __name__ == "__main__":
    chat_loop()
