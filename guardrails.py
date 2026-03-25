import re
from fastapi import HTTPException
from config import MAX_PROMPT_LENGTH

BLOCKED_PATTERNS = [
    r"ignore.*previous",
    r"disregard.*instructions",
    r"reveal.*system",
    r"bypass.*safety",
]

def validate_prompt(prompt: str):
    if len(prompt) > MAX_PROMPT_LENGTH:
        raise HTTPException(status_code=400, detail="Prompt too long")

    lower_prompt = prompt.lower()

    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, lower_prompt):
            raise HTTPException(
                status_code=400,
                detail="Unsafe prompt detected"
            )