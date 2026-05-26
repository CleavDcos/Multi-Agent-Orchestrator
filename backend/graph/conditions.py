from graph.graph_state import GraphState


MAX_RETRIES = 1


# -----------------------------------
# ROUTER DECISION
# -----------------------------------

def router_condition(state: GraphState):

    selected_agent = state["selected_agent"]

    if selected_agent == "Coding":
        return "coding"

    elif selected_agent == "Testing":
        return "testing"

    else:
        return "research"
    
#create normal router condition, ie from state, whatever agent we get selected, return  its name 
#eg Router -> Research Node -> END


# -----------------------------------
# TESTING DECISION
# -----------------------------------

def testing_condition(state: GraphState):

    testing_response = state["testing_response"]

    retry_count = state["retry_count"]

    if (
        "ISSUES FOUND:" in testing_response
        and retry_count < MAX_RETRIES
    ):

        state["retry_count"] += 1

        return "retry"

    return "approved"

#We have a CONDITION for testing Node
#If testing has issues, retry, if not then approcve. 
 


