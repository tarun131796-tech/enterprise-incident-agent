from fastapi import Header, HTTPException
import os

API_KEY = os.getenv("SERVICE_API_KEY", "secret123")


def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
