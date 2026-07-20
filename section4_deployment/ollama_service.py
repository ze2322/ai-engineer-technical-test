from ollama import Client


class OllamaService:

    def __init__(self):

        self.client = Client(
            host="http://localhost:11434"
        )

        self.model = "llama3.2"

    def generate(self, prompt: str):

        response = self.client.chat(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],

        )

        return response["message"]["content"]