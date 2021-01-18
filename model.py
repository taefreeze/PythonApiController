from pydantic import BaseModel
from typing import Optional
import requests
from fastapi import Request, FastAPI
from typing import Optional


class ServiceRegisterModel(BaseModel):
    service_name: str
    api_url: str
    permission: str
    user_id: str

class UserLoginModel(BaseModel):
    id : str

class ServiceDeleteModel(BaseModel):
    id : str