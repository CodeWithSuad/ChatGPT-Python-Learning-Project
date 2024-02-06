from openai import OpenAI
import requests
import os

api_key = os.environ.get("OPENAI_API_KEY")


def openai_client_chat(messages):
    """
    Interacts with the ChatGPT model using the OpenAI Python client library.

    :param messages: List containing conversation history between user and ChatGPT.
                                Each message is a dictionary with keys "role" and "content".
    :return: None.
    """
    client = OpenAI(api_key=api_key)
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
    )
    messages.append(chat_completion.choices[0].message)
    print("Response from ChatGPT: \n", chat_completion.choices[0].message.content, "\n")


def http_request_chat(messages):
    """
    Interacts with the ChatGPT model by making HTTP requests directly to the OpenAI API endpoint.

    :param messages: List containing conversation history between user and ChatGPT.
                                Each message is a dictionary with keys "role" and "content".
    :return: None.
    """
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "model" : "gpt-3.5-turbo",
        "messages": messages
    }

    res = requests.post(url, headers=headers, json=data)
    # if the request was successful
    if res.status_code == 200:
        response = res.json()
        messages.append(response['choices'][0]['message'])
        print("Response from ChatGPT: \n", response['choices'][0]['message']['content'], "\n")
    else:
        print("Error:", res.status_code, res.text)


if __name__=="__main__":
    messages_memory = []
    while True:
        # The memory is limited to 10 messages (including both user inputs and model responses)
        if len(messages_memory) > 10:
            messages_memory.pop(0)

        prompt = input("Message ChatGPT...\n")
        new_message = {
            "role": "user",
            "content": prompt
        }
        messages_memory.append(new_message)
        # Choose between two interaction approaches: OpenAI Python client or direct HTTP requests.
        http_request_chat(messages_memory)
