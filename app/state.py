from typing import TypedDict, Optional


class AgentState(TypedDict):
    tenant_id: str
    incident: str
    category: Optional[str]
    result: Optional[str]
