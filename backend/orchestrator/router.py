from agents.coding_agent import CodingAgent
from agents.testing_agent import TestingAgent
from agents.research_agent import ResearchAgent
from memory.conversation_memory import ConversationMemory
from orchestrator.llm_router import LLMRouter

class AgentRouter:
    def __init__(self):
        #agent objects
        self.coding_agent = CodingAgent()
        self.conversation_memory = ConversationMemory()
        self.testing_agent = TestingAgent()
        self.research_agent = ResearchAgent()
        self.llm_router = LLMRouter()

    async def route(self,user_input:str, session_id:str):
  
        #First save into memory user request
        self.conversation_memory.save_message(
            session_id,
            "user",
            user_input
        )
        conversation_history = self.conversation_memory.get_conversation(session_id) 

        #Create a list of possible words for routing
        selected_agent_name = await self.llm_router.decide_agent(user_input)

        if selected_agent_name == "Coding Agent":
            selected_agent = self.coding_agent

        elif selected_agent_name == "Testing Agent":
            selected_agent = self.testing_agent

        else:
            selected_agent = self.research_agent
  
        #call the execute function of base agent (call for selected agent n pass the input)
        response = await selected_agent.execute(user_input)
        #used await because execute is async functon and may take some time to perform its functin
        #in our case , AI Takes time 


        #then save into memory the agent response
        self.conversation_memory.save_message(
            session_id,
            "assistant",
            response
        )

        return {
            "selected_agent": selected_agent.name,
            "role": selected_agent.role,
            "conversation_history": conversation_history,
            "response": response
        }
    #return structured response

    