import ollama
from app.rag.pinecone_client import get_index


def retrieve(query: str, tenant_id: str) -> str:
    idx = get_index()

    emb = ollama.embeddings(model="nomic-embed-text", prompt=query)["embedding"]

    res = idx.query(
        vector=emb,
        top_k=1,
        include_metadata=True,
        namespace=tenant_id,  # 🔥 tenant isolation
    )

    if not res["matches"]:
        return "No relevant SOP found."

    return res["matches"][0]["metadata"]["text"]
