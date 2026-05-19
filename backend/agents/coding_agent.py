from agents.base_agent import BaseAgent

class CodingAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Coding Agent",
            role ="Software Engineering Specialist",
            system_prompt="""
            You are an expert software engineer.
            You write clean, scalable, production-ready code.
            Always explain your reasoning clearly.
        """
        )
#Above we use inheritance to use baseagent the parent class
#sper calls parennt class
#the super encapsulates all things to pass to Parent class