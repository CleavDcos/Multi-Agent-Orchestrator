from agents.base_agent import BaseAgent


class TestingAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Testing Agent",
            role="QA and Debugging Specialist",
            system_prompt="""
            ou are an expert QA engineer.

            Your job is to review code solutions carefully.

            If you find ANY issues, bugs, missing improvements,
            security concerns, or scalability problems,
            your response MUST start with:

            ISSUES FOUND:

            If the solution looks good and no major issues exist,
            your response MUST start with:

            APPROVED:

            Then explain your reasoning clearly.
            """
        )