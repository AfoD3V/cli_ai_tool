import requests
import os
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
import typer

class ChatBot:
    """
    A class that interacts with the DeepInfra API to create a chat bot.
    
    This class handles API communication, message history management,
    and provides methods to send prompts and receive responses.
    
    Attributes:
        model (str): The LLM model to use for generating responses.
        token (str): API key for authentication.
        url (str): The endpoint URL for the DeepInfra API.
        headers (dict): HTTP headers for API requests.
        messages (list): Conversation history.
    """
    
    def __init__(self, model="meta-llama/Meta-Llama-3-8B-Instruct", system_instruction="You are friendly assistant"):
        """
        Initialize a ChatBot instance.
        
        Args:
            model (str, optional): The LLM model to use. Defaults to "meta-llama/Meta-Llama-3-8B-Instruct".
            system_instruction (str, optional): Initial system message. Defaults to "You are friendly assistant".
        
        Raises:
            ValueError: If API_KEY environment variable is not found.
        """
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
        """
        Return a string representation of the ChatBot instance.
        
        Returns:
            str: The model name.
        """
        return f"{self.model}"
    
    def _get_api_key(self):
        """
        Retrieve API key from environment variables.
        
        Returns:
            str: The API key.
            
        Raises:
            ValueError: If API_KEY is not found in environment variables.
        """
        load_dotenv()
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY not found in environment variables.")
        return api_key
    
    def ask(self, prompt_message):
        """
        Send a prompt to the LLM and get a response.
        
        This method updates the conversation history with the user's prompt
        and the assistant's response.
        
        Args:
            prompt_message (str): The user's input message.
            
        Returns:
            str: The assistant's response.
            
        Raises:
            RuntimeError: If the API request fails or returns an error.
        """
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
    """
    Command Line Interface for interacting with the ChatBot.
    
    This class provides a simple terminal interface for sending prompts
    to the ChatBot and displaying the responses.
    
    Attributes:
        chatbot (ChatBot): The ChatBot instance.
        console (Console): Rich console for formatted output.
    """
    
    def __init__(self, chat_bot):
        """
        Initialize a CLI instance.
        
        Args:
            chat_bot (ChatBot): A ChatBot instance to handle the conversation.
        """
        self.chatbot = chat_bot
        self.console = Console()

    def run(self):
        """
        Start the command line interface.
        
        This method runs an input loop that:
        1. Takes user input
        2. Sends it to the ChatBot
        3. Displays the formatted response
        
        The loop continues until the user types 'exit'.
        
        Exception handling is implemented to catch and display errors.
        """
        self.console.print("[bold green]Chatbot is ready! Type 'exit' to quit.[/bold green]")
        while True:
            user_input = input("Prompt: ")
            if user_input.lower() == "exit":
                self.console.print(f"[bold red]Bye![/bold red]")
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

def main(
        model: str = typer.Option("meta-llama/Meta-Llama-3-8B-Instruct",
                                    help="Model to use for the chatbot."),
        system: str = typer.Option("You are friendly assistant",
                                    help="Option to adjust how model is going to behave.")

):
    
    bot = ChatBot(model=model)
    cli = CLI(chat_bot=bot)
    cli.run()

if __name__ == "__main__":
    typer.run(main)