import redis
from fastapi import HTTPException
from config import RATE_LIMIT, RATE_WINDOW

r = redis.Redis(host='localhost', port=6379, db=0)

def check_rate_limit(api_key: str):
    key = f"rate_limit:{api_key}"

    current = r.incr(key)
    
    print("🔥 NEW VERSION LOADED 🔥")
    print("FUNCTION LOADED")
    print("KEY:", key)
    print("CURRENT COUNT:", current)

    if current == 1:
        r.expire(key, RATE_WINDOW)

    if current > RATE_LIMIT:
        print("RATE LIMIT TRIGGERED")
        raise HTTPException(status_code=429, detail="Rate limit exceeded")