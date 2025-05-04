import requests
import os
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown

class ChatBot:
    def __init__(self, model="meta-llama/Meta-Llama-3-8B-Instruct", system_instruction="You are friendly assistant"):
        self.model = model
        self.token = self._get_api_key()
        self.url = "https://api.deepinfra.com/v1/openai/chat/completions"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        self.messages = [
            {
                "role": "system",
                "content": system_instruction
            }
        ]

    def __str__(self):
        return f"{self.model}"
    
    def _get_api_key(self):
        load_dotenv()
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY not found in environment variables.")
        return api_key
    
    def ask(self, prompt_message):
        self.messages.append({"role": "user", "content": prompt_message})
        response = requests.post(self.url, headers=self.headers, json={
            "model": self.model,
            "messages": self.messages 
        })
        if response.status_code == 200 and response.json()['choices'][0]['message']['content'] != "":
            answer = response.json()['choices'][0]['message']['content']
            self.messages.append({
                "role": "assistant",
                "content": answer
            })
            return answer
        else:
            if response.json()['choices'][0]['message']['content'] == "":
                print("Empty prompt! Re-enter your prompt!")
            else:
                raise RuntimeError(
                f"API Error {response.status_code}: {response.text}"
            )
    
class CLI:
    def __init__(self, chat_bot):
        self.chatbot = chat_bot
        self.console = Console()

    def run(self):
        self.console.print("[bold green]Chatbot is ready! Type 'exit' to quit.[/bold green]")
        while True:
            user_input = input("Prompt: ")
            if user_input.lower() == "exit":
                break
            elif user_input == "":
                print("Empty prompt, please re-enter...")
                continue
            else:
                try:
                    response = self.chatbot.ask(user_input)
                    self.console.print(Markdown(response))
                except Exception as e:
                    self.console.print(f"[bold red]Error:[/bold red] {e}")

if __name__ == "__main__":
    bot = ChatBot()
    cli = CLI(chat_bot=bot)
    cli.run()

