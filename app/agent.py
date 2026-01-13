from langgraph.graph import StateGraph, END
from app.state import AgentState
from app.classifier import classify
from app.tools.log_analyzer import analyze_log
from app.rag.retriever import retrieve
from app.escalation import should_escalate


# --- Nodes ---


def escalation_node(state):
    state["result"] = (
        "Escalated to L2 support agent. Additional investigation required."
    )
    return state


def classify_node(state: AgentState):
    state["category"] = classify(state["incident"])
    return state


def log_node(state: AgentState):
    state["result"] = analyze_log(state["incident"])
    return state


def sop_node(state):
    state["result"] = retrieve(state["incident"], state["tenant_id"])
    return state


def default_node(state: AgentState):
    state["result"] = "Incident noted. No automated action required."
    return state


# --- Router ---


def route(state):
    if state["result"] and should_escalate(state["result"]):
        return "escalate"
    return state["category"]


# --- Graph ---

graph = StateGraph(AgentState)

graph.add_node("classify", classify_node)
graph.add_node("log", log_node)
graph.add_node("sop", sop_node)
graph.add_node("default", default_node)

graph.set_entry_point("classify")

graph.add_conditional_edges(
    "classify",
    route,
    {
        "LOG_ANALYSIS": "log",
        "SOP_LOOKUP": "sop",
        "GENERAL_REASONING": "default",
        "CALCULATION": "default",
    },
)

graph.add_edge("log", END)
graph.add_edge("sop", END)
graph.add_edge("default", END)

agent = graph.compile()
