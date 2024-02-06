from openai import OpenAI
import requests
import os

api_key = os.environ.get("OPENAI_API_KEY")

def openai_client_chat(messages_memory):

    client = OpenAI(api_key=api_key)
    chat_completion = client.chat.completions.create(
        messages=messages_memory,
        model="gpt-3.5-turbo",
    )
    messages_memory.append(chat_completion.choices[0].message)
    print("Response from ChatGPT: \n", chat_completion.choices[0].message.content, "\n")

def http_request_chat(messages_memory):
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "model" : "gpt-3.5-turbo",
        "messages": messages_memory
    }
    res = requests.post(url, headers=headers, json=data)
    #if the request was successful
    if res.status_code == 200:
        response = res.json()
        messages_memory.append(response['choices'][0]['message'])
        print("Response from ChatGPT: \n", response['choices'][0]['message']['content'], "\n")
    else:
        print("Error:", res.status_code, res.text)


messages_memory = []
while True:
    #The memory is limited to 10 messages (including both user inputs and model responses)
    if len(messages_memory) > 10:
        messages_memory.pop(0)

    prompt = input("Message ChatGPT...\n")
    new_message = {
        "role": "user",
        "content": prompt
    }
    messages_memory.append(new_message)
    #Here you can choose between the two approaches (OpenAI Client or HTTP Requests)
    http_request_chat(messages_memory)
