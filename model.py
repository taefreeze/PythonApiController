from pydantic import BaseModel
from typing import Optional
import requests
from fastapi import Request, FastAPI
from typing import Optional


class Register(BaseModel):
    service_name: str
    api_url: str
    permission: str
    user_id: str

class User(BaseModel):
    id : str