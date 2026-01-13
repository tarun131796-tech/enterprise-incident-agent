def should_escalate(text: str) -> bool:
    triggers = ["unknown", "not sure", "cannot determine"]
    return any(t in text.lower() for t in triggers)
