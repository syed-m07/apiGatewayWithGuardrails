from fastapi import FastAPI, Header, HTTPException
from auth import validate_api_key
from guardrails import validate_prompt
from rate_limiter import check_rate_limit
from pydantic import BaseModel
from llm_client import generate_response
from logger import log_request
from cache import get_cached_response, set_cached_response
import time
import os

print("🔥 MAIN FILE PATH:", os.path.abspath(__file__))

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate(data: PromptRequest, authorization: str = Header(None)):
    
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")

    api_key = authorization.replace("Bearer ", "").strip()
    prompt = data.prompt

    # 1. Auth
    validate_api_key(api_key)

    # 2. Rate Limit
    check_rate_limit(api_key)

    # 3. Guardrails
    validate_prompt(prompt)

    # 4. Caching
    cached = get_cached_response(prompt)

    if cached:
        log_request(api_key, prompt, time.time())
        return {"response": cached.decode(), "cached": True}

    start = time.time()

    # 5. LLM
    response = generate_response(prompt)

    # 6. Cache store
    set_cached_response(prompt, response)

    # 7. Logging
    log_request(api_key, prompt, start)

    return {
        "response": response,
        "cached": False
    }