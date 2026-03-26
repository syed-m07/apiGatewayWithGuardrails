import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def get_cached_response(prompt: str):
    return r.get(f"cache:{prompt}")

def set_cached_response(prompt: str, response: str):
    r.setex(f"cache:{prompt}", 300, response)  # 5 min cache