# ChatGPT Interaction Documentation

## Overview

This documentation provides an overview and usage guide for interacting with the ChatGPT model using Python code. The code allows for two different approaches for interacting with ChatGPT: using the OpenAI Python client library and making HTTP requests directly.

## Prerequisites

Before using this code, ensure you have the following prerequisites installed:

- Python 3.x
- `openai` Python library (`pip install openai`)
- `requests` library (`pip install requests`)

## Configuration

To use the code provided, you need an API key from OpenAI. Set the API key as an environment variable named `OPENAI_API_KEY`. This key is necessary for authenticating requests to the OpenAI API.

## Code Structure

The provided code consists of two functions for interacting with ChatGPT:

1. `openai_client_chat(messages)`: This function uses the OpenAI Python client library to interact with the ChatGPT model. It sends messages to the model and retrieves responses using the OpenAI API.

2. `http_request_chat(messages_memory)`: This function interacts with the ChatGPT model by making HTTP requests directly to the OpenAI API endpoint. It constructs HTTP requests with appropriate headers and parameters and handles the responses.

The main loop in the code continuously prompts the user for input messages and passes them to one of the interaction functions based on the chosen approach.

## Usage

1. Clone or download the provided code.
2. Set up the environment variable `OPENAI_API_KEY` with your OpenAI API key.
3. Run the Python script.

Upon execution, the script will prompt you to enter messages for ChatGPT. It will then generate responses using the chosen interaction method and display them.

## Choosing Interaction Method

You can choose between two approaches for interacting with ChatGPT:

- **OpenAI Client (Recommended):** Use the `openai_client_chat` function. This approach utilizes the official OpenAI Python client library for simplified interaction with the ChatGPT model.

- **HTTP Requests:** Use the `http_request_chat` function. This approach makes HTTP requests directly to the OpenAI API endpoint. It offers more flexibility but requires more manual handling of request construction and response parsing.

## Conversation Memory

The `messages_memory` variable serves as a memory to store the conversation history between the user and the ChatGPT model. It maintains a limited history of the most recent messages (up to 10 messages), including both user inputs and model responses. This memory is utilized to provide context to the model for generating responses.

## Notes

- Ensure that your usage complies with OpenAI's API usage policies and guidelines.

For further information or assistance, refer to the OpenAI API documentation or contact OpenAI support.
