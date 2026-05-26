from typing  import Optional, TypedDict, List, Dict

class GraphState(TypedDict):

    """
    Shared state that travels through every Node.
    """


    #Original user req
    user_input: str

    #Which agent/workflow router selected
    selected_agent: Optional[str]

    #O/p from coding agent
    coding_response: Optional[str]

    #O/p from testing agent
    testing_response: Optional[str]

    #O/p from research agent
    research_response: Optional[str]

    #Number of retry attempts 
    retry_count: int

    #Final response returned to user
    final_response: Optional[str]   

    #Previosu convo history from redis, this will be seen by every node in the graph
    conversation_history: List[Dict]



#Every node will receive it.


