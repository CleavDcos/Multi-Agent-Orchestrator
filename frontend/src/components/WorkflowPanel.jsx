function WorkflowPanel({ workflowData }) {

    if (!workflowData) {

        return (

            <div className="workflow-panel">

                <h2>
                    Workflow Dashboard
                </h2>

                <p>
                    No workflow executed yet.
                </p>

            </div>
        );
    }

    return (

        <div className="workflow-panel">

            <h2>
                Workflow Dashboard
            </h2>

            <div className="workflow-card">

                <h3>
                    Selected Agent
                </h3>

                <p>
                    {workflowData.selected_agent || "N/A"}
                </p>

            </div>



            <div className="workflow-card">

                <h3>
                    Retry Count
                </h3>

                <p>
                    {workflowData.retry_count ?? 0}
                </p>

            </div>



            <div className="workflow-card">

                <h3>
                    Final Response
                </h3>

                <p>
                    {
                        workflowData.final_response ||
                        "No response generated"
                    }
                </p>

            </div>

        </div>
    );
}

export default WorkflowPanel;