from agents.base_agent import BaseAgent


class TestingAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Testing Agent",
            role="QA and Debugging Specialist",
            system_prompt="""
            You are an expert QA engineer.
            You specialize in debugging, testing, and identifying issues in code.
            Always explain bugs and fixes clearly.
            """
        )