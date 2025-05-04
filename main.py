import requests
import os
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown

load_dotenv()

def get_api_key():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not found in environment variables.")
    return api_key

def prompt(prompt_text):
    url = "https://api.deepinfra.com/v1/openai/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {get_api_key()}"
    }
    data = {
        "model": "meta-llama/Meta-Llama-3-8B-Instruct",
        "messages": [
            {
                "role": "system",
                "content": "You are friendly helper, alway glad to answer all the questions"
            },
            {
                "role": "user",
                "content": f"{prompt_text}"
            }
        ]
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)

def main():
    console = Console()
    while True:
        user_input = input("Prompt: ")
        if user_input == "exit":
            break
        else:
            response = prompt(user_input)['choices'][0]['message']['content']
            if response == "":
                print("Response string is empty! Please re-type your prompt...")
                continue
            md_response = Markdown(response)
            console.print(md_response)

if __name__ == "__main__":
    main()
