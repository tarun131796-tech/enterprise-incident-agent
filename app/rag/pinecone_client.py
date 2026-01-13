import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

# 🔴 THIS LINE IS MANDATORY
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")

if not PINECONE_API_KEY:
    raise RuntimeError("PINECONE_API_KEY not loaded. Check .env file.")

pc = Pinecone(api_key=PINECONE_API_KEY)


def get_index():
    existing = [idx["name"] for idx in pc.list_indexes()]

    if PINECONE_INDEX not in existing:
        pc.create_index(
            name=PINECONE_INDEX,
            dimension=768,  # nomic-embed-text
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )

    return pc.Index(PINECONE_INDEX)
