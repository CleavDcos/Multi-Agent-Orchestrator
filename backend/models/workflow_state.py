#Create a model of what a state shud be 
#State management is being done in orchestrator, to keep track of what current phase of the multi agent system we r in
#The dashboard can use this to display the current state of the system

from pydantic import BaseModel
from typing import List

class WorkflowState(BaseModel):
    workflow_name : str
    current_step:str
    status:str
    retry_count:int = 0
    active_agent:str

    completed_steps: List[str] = []

