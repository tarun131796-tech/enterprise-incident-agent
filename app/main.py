from fastapi import FastAPI, Depends, Header
from app.agent import agent
from app.auth import verify_api_key

app = FastAPI(title="Enterprise Incident Agent")


@app.post("/analyze", dependencies=[Depends(verify_api_key)])
def analyze(payload: dict, tenant_id: str = Header(..., alias="X-Tenant-ID")):
    result = agent.invoke(
        {
            "tenant_id": tenant_id,
            "incident": payload["incident"],
            "category": None,
            "result": None,
        }
    )
    return result
