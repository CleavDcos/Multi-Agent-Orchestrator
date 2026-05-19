from openai import OpenAI
from core.config import OPENAI_API_KEY

class LLMRouter:

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    async def decide_agent(self,user_input):
        #prompt to teach router of available agents, responsibilities, rules
        #orchestration prompting
        router_prompt = f"""
        You are an intelligent AI orchestrator.

        Your job is to decide which specialized agent
        should handle the user's request.

        Available agents:

        1. Coding Agent
        - Handles coding
        - APIs
        - software development
        - programming
        - architecture

        2. Testing Agent
        - Handles bugs
        - debugging
        - testing
        - fixing issues

        3. Research Agent
        - Handles explanations
        - research
        - technical concepts
        - learning topics

        Return ONLY one of these exact values:
        - Coding Agent
        - Testing Agent
        - Research Agent

        User Request:
        {user_input}
        """

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": router_prompt
                }
            ]
        )

        return response.choices[0].message.content.strip()