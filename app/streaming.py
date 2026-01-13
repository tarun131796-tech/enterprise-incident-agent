from fastapi import APIRouter
from app.agent import agent

router = APIRouter()


@router.post("/analyze/stream")
def analyze_stream(payload: dict):
    for event in agent.stream(
        {"incident": payload["incident"], "category": None, "result": None}
    ):
        yield f"{event}\n"
