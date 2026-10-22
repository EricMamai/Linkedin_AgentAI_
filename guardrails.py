_BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "disregard your prompt",
    "jailbreak",
    "bypass restrictions",
    "ignore all instructions"
]

MIN_SCORE=6
MIN_WORDS=50
MAX_WORDS=700


def validate_input(text,max_length=500):
    if not text or not isinstance(text,str):
        raise ValueError("Input must be a non empty string")
    text = text.strip()[:max_length]
    text = text.lower()
    for pattern in _BLOCKED_PATTERNS:
        if pattern in text:
            raise ValueError(f"Input rejected: disallowed content detected ('{pattern}')")
    return text

def validate_output(post_data, validation_data):
    issues=[]
    try:
        score = float(str(validation_data.get("score",0)).split("/")[0])
        if score < MIN_SCORE:
            issues.append(f"Score below minimum threshold ({score} < {MIN_SCORE})")
    except (TypeError, ValueError):
        pass
    content = post_data.get("post_content","")
    word_count = len(content.split())
    if word_count < MIN_WORDS:
        issues.append(f"Content has only {word_count} words, below minimum of {MIN_WORDS}")
    if word_count > MAX_WORDS:
        issues.append(f"Content has {word_count} words, exceeding maximum of {MAX_WORDS}")
    cringe = validation_data.get("cringe_flags", [])
    if cringe:
        issues.append(f"Cringe flags detected: {', '.join(cringe)}")
        
    return {"passed": len(issues) ==0, "issues":issues}