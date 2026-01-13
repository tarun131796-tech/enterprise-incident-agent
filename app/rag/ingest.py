import os
import ollama
from app.rag.pinecone_client import get_index


def ingest():
    idx = get_index()

    for file in os.listdir("data/sops"):
        with open(f"data/sops/{file}", "r") as f:
            text = f.read()

        emb = ollama.embeddings(model="nomic-embed-text", prompt=text)["embedding"]

        idx.upsert([{"id": file, "values": emb, "metadata": {"text": text}}])

    print("✅ SOP ingestion completed")


if __name__ == "__main__":
    ingest()
