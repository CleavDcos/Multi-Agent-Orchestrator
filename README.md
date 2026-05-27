# Multi-Agent Orchestrator System

A full-stack AI orchestration platform built using **LangGraph, FastAPI, React, Redis, and Docker**.

This project demonstrates how multiple AI agents can collaborate inside a graph-based workflow system with shared memory, workflow routing, and containerized deployment.

---

# Features

- Multi-Agent AI Architecture
- LangGraph Workflow Orchestration
- FastAPI Backend
- React Frontend Dashboard
- Redis Shared Conversation Memory
- Workflow State Tracking
- AI Agent Routing
- Dockerized Microservices
- Real-Time Workflow Visualization
- Async API Architecture

---

# Tech Stack

## Backend
- Python
- FastAPI
- LangGraph
- OpenAI API
- Redis

## Frontend
- React
- Vite
- CSS

## Infrastructure
- Docker
- Docker Compose

---

# Architecture Overview

```text
Frontend (React)
        ↓
FastAPI Backend
        ↓
LangGraph Workflow
        ↓
Router Node
   ↙     ↓      ↘
Coding  Testing  Research
 Agent    Agent    Agent
        ↓
Redis Shared Memory
```

---

# Project Structure

```text
multi_agent/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   ├── App.jsx
│   │   └── App.css
│   │
│   └── Dockerfile
│
├── backend/
│   ├── agents/
│   ├── graph/
│   ├── memory/
│   ├── workflows/
│   ├── core/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
├── .env
└── README.md
```

---

# How It Works

## 1. User Sends Message

The React frontend sends the user query to FastAPI.

Example:

```text
"Build a scalable authentication API"
```

---

## 2. LangGraph Starts Workflow

FastAPI invokes the LangGraph workflow.

The graph:
- stores state
- manages routing
- controls agent execution

---

## 3. Router Node Selects Agent

The Router Node uses the LLM to determine which specialist agent should handle the request.

Possible agents:
- Coding Agent
- Testing Agent
- Research Agent

---

## 4. Agent Executes Task

The selected agent processes the request and generates a response.

---

## 5. Redis Stores Memory

Conversation history is stored inside Redis so all graph nodes can access shared memory.

---

## 6. Frontend Displays Workflow

The frontend dashboard visualizes:
- selected agent
- workflow status
- retry count
- final response

---

# LangGraph Workflow

The workflow is implemented using LangGraph nodes.

## Main Nodes

### Router Node
Determines which agent should execute.

### Coding Node
Generates code solutions.

### Testing Node
Reviews generated solutions.

### Research Node
Handles informational and research-based queries.

---

# Redis Memory System

Redis is used as shared memory across workflow nodes.

## Benefits
- Persistent conversations
- Shared graph state
- Scalable architecture
- Fast retrieval

---

# Dockerized Architecture

The entire system runs using Docker containers.

## Containers

- Frontend Container
- Backend Container
- Redis Container

All services communicate through Docker Compose networking.

---

# Installation

## Clone Repository

```bash
git clone <your-repo-url>
cd multi_agent
```

---

# Environment Variables

Create a `.env` file in the root directory.

```env
OPENAI_API_KEY=your_api_key
```

---

# Run Using Docker

```bash
docker compose up --build
```

---

# Frontend

```text
http://localhost:5173
```

# Backend

```text
http://localhost:8000
```

---

# Local Development Setup

## Backend

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

python -m uvicorn main:app --reload
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# API Endpoint

## POST `/chat`

### Request

```json
{
  "session_id": "demo-session",
  "message": "Explain LangGraph"
}
```

---

### Response

```json
{
  "selected_agent": "Research Agent",
  "retry_count": 0,
  "final_response": "LangGraph is..."
}
```

---

# Screenshots

## Chat Dashboard

_Add Screenshot Here_

---

## Workflow Panel

_Add Screenshot Here_

---

# Future Improvements

- ChromaDB Long-Term Memory
- Tool Calling
- Authentication
- Multi-User Sessions
- Deployment to Cloud
- Streaming Responses
- Advanced Workflow Monitoring

---

# Key Learnings

This project demonstrates:
- AI orchestration systems
- graph-based workflows
- microservice architecture
- containerization
- shared memory systems
- frontend-backend integration
- async API development

---

# Author

**Cleaven D'costa**

---

# License

MIT License