from agents.base_agent import BaseAgent


class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Research Agent",
            role="Technical Research Specialist",
            system_prompt="""
            You are a technical research expert.
            You explain technical concepts clearly and provide accurate research-based answers.
            """
        )