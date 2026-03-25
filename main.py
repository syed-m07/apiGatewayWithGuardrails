from fastapi import FastAPI, Header, HTTPException
from auth import validate_api_key
from guardrails import validate_prompt
from rate_limiter import check_rate_limit
import os
from pydantic import BaseModel
from llm_client import generate_response
import time
from logger import log_request

print("🔥 MAIN FILE PATH:", os.path.abspath(__file__))

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate(data: PromptRequest, authorization: str = Header(None)):
    
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")

    api_key = authorization.replace("Bearer ", "")

    prompt = data.prompt

    # 1. Auth
    validate_api_key(api_key)

    # 2. Rate Limit
    check_rate_limit(api_key)

    # 3. Guardrails
    validate_prompt(prompt)

    start = time.time()
    
    response = generate_response(prompt)

    log_request(api_key, prompt, start)

    return {
        "response": response
    }