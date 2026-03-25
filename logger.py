import time

def log_request(api_key, prompt, start_time):
    latency = time.time() - start_time

    print({
        "user": api_key,
        "prompt_length": len(prompt),
        "latency_sec": round(latency, 3)
    })