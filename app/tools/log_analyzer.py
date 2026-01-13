def analyze_log(text: str) -> str:
    if "503" in text:
        return "503 indicates service unavailable. Possible upstream failure or deployment issue."
    return "No known error pattern detected."
