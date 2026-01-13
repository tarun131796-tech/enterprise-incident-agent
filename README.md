# Enterprise Incident Intelligence Agent

A production-grade, SaaS-ready AI agent for real-time incident analysis.

## Tech Stack
- **Python**: Core programming language.
- **LangChain + LangGraph**: Orchestration and state management for the agent.
- **Gemini LLM**: Language model for analysis and decision making.
- **Pinecone**: Vector database for RAG (Retrieval-Augmented Generation).
- **Ollama**: Local embedding generation (`nomic-embed-text`).
- **FastAPI**: Backend API framework.
- **Streamlit**: Frontend UI for demos.
- **Docker**: Containerization.
- **LangSmith**: Observability (optional).

## Features
- Incident classification
- SOP retrieval via RAG
- Multi-agent escalation (L1 → L2)
- Streaming responses
- API key authentication
- **Tenant-aware architecture**: Data isolation per tenant using vector DB namespaces.
- Dockerized deployment
- Frontend UI for demos

## Prerequisites

Before running the application, ensure you have the following installed:

1.  **Python 3.10+**
2.  **Ollama**: Used for local embeddings.
    -   Install Ollama: https://ollama.com/
    -   Pull the embedding model:
        ```bash
        ollama pull nomic-embed-text
        ```
3.  **Pinecone Account**: You need a Pinecone API key and an index name.
4.  **Google Cloud Project**: You need a Google API key with access to Gemini models.

## Installation

1.  Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1.  Copy the example environment file:
    ```bash
    cp .env.example .env
    ```

2.  Open `.env` and fill in your API keys:
    -   `GOOGLE_API_KEY`: Your Google Gemini API Key.
    -   `PINECONE_API_KEY`: Your Pinecone API Key.
    -   `PINECONE_INDEX`: The name of your Pinecone index.
    -   `SERVICE_API_KEY`: (Optional) The API key for the backend service (defaults to `secret123`).

## Data Ingestion

To make the agent useful, you need to ingest Standard Operating Procedures (SOPs) into the vector database. The system supports multi-tenancy, so you must specify a Tenant ID.

1.  Place your SOP text files in the `data/sops/` directory.
2.  Run the ingestion script:

    ```bash
    python -m app.rag.ingest --tenant-id <your-tenant-id>
    ```
    Example:
    ```bash
    python -m app.rag.ingest --tenant-id tenant-1
    ```
    This indexes the documents in `data/sops/` and stores them in Pinecone under the namespace `tenant-1`.

## Running the Application

### 1. Start the Backend API

```bash
uvicorn app.main:app --reload
```
The API will be available at `http://localhost:8000`.

### 2. Start the Frontend UI

```bash
streamlit run frontend.py
```
The UI will open in your browser (typically at `http://localhost:8501`).

## Usage

1.  Open the Streamlit UI.
2.  Enter the **Tenant ID** you used during data ingestion (e.g., `tenant-1`).
3.  Describe an incident (e.g., "API is returning 503 errors").
4.  Click **Analyze**.
5.  The agent will classify the incident, retrieve relevant SOPs (scoped to that tenant), and provide a recommendation.

## API Endpoints

-   `POST /analyze`: Main endpoint for incident analysis.
    -   Headers:
        -   `x-api-key`: Authentication key.
        -   `X-Tenant-ID`: Tenant identifier.
    -   Body:
        -   `incident`: Description of the incident.
