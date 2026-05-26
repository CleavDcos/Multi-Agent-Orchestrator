from backend import memory
from fastapi import FastAPI
from pydantic import BaseModel
from memory.redis_memory import RedisMemory

from graph.graph_builder import graph


app = FastAPI()
memory = RedisMemory() #create redis memory


class UserRequest(BaseModel):
    session_id: str
    message: str


@app.get("/")
async def root():
    return {
        "message": "Multi Agent System Backend running"
    }


@app.post("/chat")
async def chat(request: UserRequest):
 
    #Load memory before the graph runs
    conversation_history = memory.get_conversation(
        request.session_id
    )

    initial_state = {
        "user_input": request.message,

        "selected_agent": None,

        "coding_response": None,

        "testing_response": None,

        "research_response": None,

        "retry_count": 0,

        "final_response": None
    }

    result = await graph.ainvoke(
        initial_state
    )
    #After the convo in graph, save the asistant response back to redis server
    memory.save_message(
    request.session_id,
    "assistant",
    result["final_response"]
)

    return result