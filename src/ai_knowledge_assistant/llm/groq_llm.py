from groq import Groq

from ai_knowledge_assistant.llm.base import LLM


class GroqLLM(LLM):

    def __init__(self, model_name,api_key):
        self.model_name = model_name

        if not api_key:
            raise ValueError("GROQ_API_KEY is missing")

        self.client = Groq(
            api_key=api_key
        )

    def generate(self, prompt):

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        return response.choices[0].message.content