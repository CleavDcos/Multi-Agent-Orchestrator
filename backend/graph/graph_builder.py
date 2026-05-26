from langgraph.graph import StateGraph, START, END
from graph.graph_state import GraphState
from graph.nodes import (
    router_node,
    coding_node,
    testing_node,
    research_node,
    finalize_node
)
from graph.conditions import (
    router_condition,
    testing_condition,
)
#Create Graph
builder = StateGraph(GraphState)

#Add Nodes

builder.add_node(
    "router",
    router_node
)
builder.add_node(
    "coding",
    coding_node
)
builder.add_node(
    "testing",
    testing_node
)
builder.add_node(
    "research",
    research_node
)
builder.add_node(
    "finalize",
    finalize_node
)

#Start edge
builder.add_edge(
    START,
    "router"
)

#Router Decision
builder.add_conditional_edges(
    "router",
    router_condition,
    {
        "coding": "coding",
        "testing": "testing",
        "research": "research"
    }
)

#Coding flow
builder.add_edge(
    "coding",
    "testing"
)

#Testing flow
builder.add_conditional_edges(
    "testing",
    testing_condition,
    {
        "retry": "coding",
        "approved": "finalize"
    }
)

#Research flow
builder.add_edge(
    "research",
    END
)

#finalize flow
builder.add_edge(
    "finalize",
    END
)

#compile graph
graph = builder.compile()