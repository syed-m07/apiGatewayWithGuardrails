print("AUTH FILE LOADING")

from fastapi import HTTPException
from config import VALID_API_KEYS

def validate_api_key(api_key: str):
    print("FUNCTION LOADED")
    if not (api_key == "test123" or api_key.startswith("user")):
        raise HTTPException(status_code=401, detail="Invalid API Key")