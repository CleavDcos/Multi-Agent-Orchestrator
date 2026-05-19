from openai import OpenAI
from core.config import OPENAI_API_KEY

#Blueprint for all agents
class BaseAgent:
    def __init__(self,name,role,system_prompt):
        self.name=name
        self.role=role
        self.system_prompt=system_prompt
        self.client=OpenAI(api_key=OPENAI_API_KEY)

    async def execute(self,user_input):
        #to be implemented by all agents
        response = self.client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [
                {
                    "role": "system",
                    "content": self.system_prompt
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        return response.choices[0].message.content
    