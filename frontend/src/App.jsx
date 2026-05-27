import { useState, useEffect, useRef } from "react";
import { sendMessage } from "./services/api";

import "./App.css";
import WorkflowPanel from "./components/WorkflowPanel";


function App() {

  // Chat messages shown on screen
  const [messages, setMessages] = useState([]);
  useEffect(() => {

  messagesEndRef.current?.scrollIntoView({
    behavior: "smooth"
  });

}, [messages]);

  // Input box value
  const [input, setInput] = useState("");
  useEffect(() => {

  messagesEndRef.current?.scrollIntoView({
    behavior: "smooth"
  });

}, [messages]);

  // Loading state while waiting for backend
  const [loading, setLoading] = useState(false);
  useEffect(() => {

  messagesEndRef.current?.scrollIntoView({
    behavior: "smooth"
  });

}, [messages]);

  // Session ID for Redis memory
  const [sessionId] = useState("demo-session");
  useEffect(() => {

  messagesEndRef.current?.scrollIntoView({
    behavior: "smooth"
  });

}, [messages]);

  // Workflow information
  const [workflowData, setWorkflowData] = useState(null);
  const messagesEndRef = useRef(null);



  async function handleSend() {

    if (!input.trim()) return;

    const userMessage = {
      role: "user",
      content: input
    };

    // Add user message immediately
    setMessages((prev) => [
      ...prev,
      userMessage
    ]);

    setLoading(true);

    try {
      //call to api.js which calls the backend to send user request and receive response
      const result = await sendMessage(
        sessionId,
        input
      );
      //result stores assistant message
      const assistantMessage = {
        role: "assistant",
        content:
          result.final_response ||
          JSON.stringify(result)
      };

      setMessages((prev) => [
        ...prev,
        assistantMessage
      ]);

      setWorkflowData(result);

    } catch (error) {

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "Error communicating with backend."
        }
      ]);

      console.error(error);

    } finally {

      setLoading(false);
      setInput("");
    }
  }



  return (

    <div className="app-container">

      <div className="chat-section">

        <h1>
          Multi-Agent Orchestrator
        </h1>

        <p>
          Session ID: {sessionId}
        </p>

        <div className="messages-container">

          {messages.map((message, index) => (

            <div
              key={index}
              className={`message ${message.role}`}
            >

              <strong>
                {message.role === "user"
                  ? "You"
                  : "Assistant"}
              </strong>

              <p>{message.content}</p>

            </div>

          ))}
          <div ref={messagesEndRef}></div>
          {loading && (

  <div className="message assistant">

    <div className="typing-indicator">

      <span></span>
      <span></span>
      <span></span>

    </div>

  </div>

)}

        </div>



        <div className="input-container">

          <input
            type="text"
            placeholder="Ask something..."
            value={input}
            onChange={(e) =>
              setInput(e.target.value)
            }
          />

          <button
            onClick={handleSend}
          >
            Send
          </button>

        </div>

      </div>



      <WorkflowPanel
  workflowData={workflowData}
/>

    </div>

  );
}

export default App;