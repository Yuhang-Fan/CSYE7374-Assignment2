# Tool Calling Chatbot

This project is a simple chatbot built in Python. It can call external tools when needed. The chatbot uses OpenAI's GPT model and supports the following functions:

- Calculator (supports sin, cos, log, etc.)
- Current time lookup

## Features

- Command-line interface
- Tool calling via OpenAI function calling
- Basic error handling
- Logs conversation history

## Project Structure

CSYE7374-Assignment2/
├── main.py         # Main chat logic
├── tools.py        # Calculator and time tools
├── config.py       # API key settings
├── requirements.txt
└── README.md

## Setup

1. Install dependencies:

   pip install -r requirements.txt

2. Set your OpenAI API key in `config.py`:

   OPENAI_API_KEY = "your-key-here"
   MODEL = "gpt-4"

## Run the Bot

In terminal:

   python main.py

Type "exit" to quit.

## Tool Examples

Calculator examples:

- sin(30)
- sqrt(16)
- log(100, 10)
- (3 + 4) * 5

Time examples:

- What time is it in Tokyo?
- Current time in UTC
- Show me the time in New York


## Limitations

- Web search has been disabled.
- Tool chaining not implemented.
- No GUI.

## API Note

This project uses OpenAI's function calling (tool calling). Make sure your model supports this feature.

## License

This code is for educational use.
