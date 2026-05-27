from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from memory.redis_memory import RedisMemory

from graph.graph_builder import graph


app = FastAPI()
#CORS config, this prevents browser from blocking communication bw frontend and backened
app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)
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

    # Load previous conversation from Redis
    conversation_history = memory.get_conversation(
        request.session_id
    )

    # Save current user message
    memory.save_message(
        request.session_id,
        "user",
        request.message
    )

    initial_state = {
        "user_input": request.message,

        "selected_agent": None,

        "coding_response": None,

        "testing_response": None,

        "research_response": None,

        "retry_count": 0,

        "final_response": None,

        "conversation_history": conversation_history
    }

    # Execute LangGraph
    result = await graph.ainvoke(
        initial_state
    )

    # Save assistant response AFTER graph finishes
    memory.save_message(
        request.session_id,
        "assistant",
        result["final_response"]
    )

    return result