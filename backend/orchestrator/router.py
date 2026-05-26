from agents.coding_agent import CodingAgent
from agents.testing_agent import TestingAgent
from agents.research_agent import ResearchAgent
from backend.memory.redis_memory import ConversationMemory
from orchestrator.llm_router import LLMRouter
from workflows.coding_workflow import CodingWorkflow

class AgentRouter:
    def __init__(self):
        #agent objects
        self.coding_agent = CodingAgent()
        self.conversation_memory = ConversationMemory()
        self.testing_agent = TestingAgent()
        self.research_agent = ResearchAgent()
        self.llm_router = LLMRouter()
        self.coding_workflow = CodingWorkflow()

    async def route(self,user_input:str, session_id:str):
  
        #First save into memory user request
        self.conversation_memory.save_message(
            session_id,
            "user",
            user_input
        )
        #Retrieve convo memory for context (can be used for better routing decisions and agent responses)

        conversation_history = self.conversation_memory.get_conversation(session_id) 

        # ASK LLMRouter which workflow should handle the request
        selected_agent_name = await self.llm_router.decide_agent(user_input)

        if selected_agent_name == "Coding Agent":
            selected_agent = self.coding_agent
            workflow_response = await self.coding_workflow.run(user_input)
            final_response = workflow_response
            system_used = "Coding Workflow"


        
        else:
            final_response = await selected_agent.execute(user_input)
            system_used = 'Research Agent'

        # then save into memory the agent response
        response = await selected_agent_name.execute(user_input)
        #used await because execute is async functon and may take some time to perform its functin
        #in our case , AI Takes time 


        #then save into memory the agent response
        self.conversation_memory.save_message(
            session_id,
            "assistant",
            str(final_response)
        )

        return {
            "system_used": system_used,
            "conversation_history": conversation_history,
            "response": final_response
        }
    #return structured response

    