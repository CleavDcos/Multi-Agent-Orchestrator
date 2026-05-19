from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator.router import AgentRouter



app = FastAPI()
router = AgentRouter()


class UserRequest(BaseModel):
    message: str


@app.get("/")
async def root():
    return {"message":"Multi Agent System Backend running"}

@app.post("/chat")
async def chat(request: UserRequest):
    response = await router.route(request.message)

    return response