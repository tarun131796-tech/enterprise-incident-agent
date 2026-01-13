# Enterprise Incident Intelligence Agent

A production-grade, SaaS-ready AI agent for real-time incident analysis.

## Tech Stack
- Python
- LangChain + LangGraph
- Gemini LLM
- Pinecone (Vector DB)
- Ollama (Local Embeddings)
- FastAPI
- Docker
- LangSmith (Observability)

## Features
- Incident classification
- SOP retrieval via RAG
- Multi-agent escalation (L1 → L2)
- Streaming responses
- API key authentication
- Tenant-aware architecture
- Dockerized deployment
- Frontend UI for demos

## Run Locally
```bash
uvicorn app.main:app --reload
