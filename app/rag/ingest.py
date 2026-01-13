import os
import argparse
import ollama
from app.rag.pinecone_client import get_index


def ingest(tenant_id):
    try:
        idx = get_index()
    except Exception as e:
        print(f"Error connecting to Pinecone: {e}")
        return

    sops_dir = "data/sops"
    if not os.path.exists(sops_dir):
        print(f"Directory {sops_dir} not found.")
        return

    for file in os.listdir(sops_dir):
        with open(f"{sops_dir}/{file}", "r") as f:
            text = f.read()

        try:
            emb = ollama.embeddings(model="nomic-embed-text", prompt=text)["embedding"]

            # Upsert with tenant_id as namespace
            idx.upsert(
                vectors=[{"id": file, "values": emb, "metadata": {"text": text}}],
                namespace=tenant_id
            )
            print(f"Upserted {file}")
        except Exception as e:
            print(f"Error processing {file}: {e}")

    print(f"✅ SOP ingestion completed for tenant: {tenant_id}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest SOPs into Pinecone for a specific tenant.")
    parser.add_argument("--tenant-id", type=str, required=True, help="The Tenant ID to ingest data for.")

    args = parser.parse_args()
    ingest(args.tenant_id)
