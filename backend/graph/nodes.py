#Each function here represents a node
#every node receives GraphState, reads data, modifies data and returns updated state

from graph.graph_state import GraphState

from agents.coding_agent import CodingAgent
from agents.testing_agent import TestingAgent
from agents.research_agent import ResearchAgent

from openai import OpenAI
from core.config import OPENAI_API_KEY

coding_agent = CodingAgent()
testing_agent = TestingAgent()
research_agent = ResearchAgent()

client = OpenAI(api_key=OPENAI_API_KEY)


#---Router Node---
async def router_node(state: GraphState):

    user_input = state["user_input"]

    router_prompt = f"""
    You are an AI Router.

    Decide which agent specialist should handle this requets.

    Available Options:
    -Coding Agent
    -Testing Agent
    -Research Agent

    Return ONLY ONE WORD:
    Coding
    Testing
    Research

    Request:
    {user_input}

 
    """
    response = client.chat.completions.create(
        model = "gpt-4.1-mini",
        messages = [
            {"role": "system", "content": router_prompt}
        ]
    )
    selected_agent = response.choices[0].message.content.strip()

    state["selected_agent"] = selected_agent    

    return state


#---Coding Node---

async def coding_node(state: GraphState):

    #Coding node know has memory to previous convo, able to understand context now
    history = state["conversation_history"]

    user_input = f"""
    Conversation History:
    {history}

   Current Request:
   {state["user_input"]}
   """


    coding_response = await coding_agent.execute(user_input)
 
    #store back in state for downstream nodes to receive it , as state is passed 
    state["coding_response"] = coding_response  

    return state

#---Testing Node---

async def testing_node(state: GraphState):
    testing_prompt = f"""
    Review this solution.

    Solution:
    {state["coding_response"]}

    If issues exist start response with:

    ISSUES FOUND:

    Otherwise start response with:

    APPROVED:
    """

    testing_response = await testing_agent.execute(
        testing_prompt
    )

    state["testing_response"] = testing_response

    return state


#---Research Node---
async def research_node(state: GraphState):

    history = state["conversation_history"]

    user_input = f"""
Conversation History:
{history}

Current Request:
{state["user_input"]}
"""

    

    research_response = await research_agent.execute(
        user_input
    )

    state["research_response"] = research_response

    state["final_response"] = research_response

    return state

#---Final Node---
async def finalize_node(state: GraphState):

    state["final_response"] = state["coding_response"]

    return state



