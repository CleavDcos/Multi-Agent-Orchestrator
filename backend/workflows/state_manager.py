#Create a state manager to keep track of the current state of the system, and to update the state as the system progresses through different phases`

from models.workflow_state import WorkflowState


class WorkflowStateManager:

    def create_state(
        self,
        workflow_name: str
    ):

        return WorkflowState(
            workflow_name=workflow_name,
            current_step="INITIALIZED",
            status="RUNNING",
            active_agent="NONE"
        )

    def update_step(
        self,
        state: WorkflowState,
        step: str,
        agent: str
    ):

        state.current_step = step
        state.active_agent = agent

        if step not in state.completed_steps:
            state.completed_steps.append(step)

        return state

    def increment_retry(
        self,
        state: WorkflowState
    ):

        state.retry_count += 1

        return state

    def complete(
        self,
        state: WorkflowState
    ):

        state.status = "COMPLETED"

        return state

    def fail(
        self,
        state: WorkflowState
    ):

        state.status = "FAILED"

        return state
