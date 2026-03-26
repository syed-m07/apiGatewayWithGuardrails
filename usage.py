import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def increment_usage(api_key: str, prompt: str):
    key = f"usage:{api_key}"

    r.hincrby(key, "requests", 1)
    r.hincrby(key, "characters", len(prompt))

def get_usage(api_key: str):
    key = f"usage:{api_key}"
    return r.hgetall(key)

def estimate_cost(characters: int):
    # rough approximation
    return round(characters / 1000 * 0.002, 4)