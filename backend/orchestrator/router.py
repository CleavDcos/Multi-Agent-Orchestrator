from agents.coding_agent import CodingAgent
from agents.testing_agent import TestingAgent
from agents.research_agent import ResearchAgent

class AgentRouter:
    def __init__(self):
        #agent objects
        self.coding_agent = CodingAgent()
        self.testing_agent = TestingAgent()
        self.research_agent = ResearchAgent()

    async def route(self,user_input:str):

        user_input_lower = user_input.lower()   
        #Create a list of possible words for routing
        if any(word in user_input_lower for word in [
            "build",
            "create",
            "develop",
            "code",
            "api",
            "develop"
        ]):
            selected_agent = self.coding_agent

        elif any(word in user_input_lower for word in [
            "test",
            "testing",
            "debug",
            "bug",
            "fix",
            "issue",
            "error"
        ]):
            selected_agent = self.testing_agent

        else:
            selected_agent = self.research_agent
  
        #call the execute function of base agent (call for selected agent n pass the input)
        response = await selected_agent.execute(user_input)
        #used await because execute is async functon and may take some time to perform its functin
        #in our case , AI Takes time 

        return {
            "selected_agent": selected_agent.name,
            "role": selected_agent.role,
            "response": response
        }
    #return structured response

    