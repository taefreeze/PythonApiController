from pydantic import BaseModel
from typing import Optional
import requests
from fastapi import Request, FastAPI
from typing import Optional


class Register(BaseModel):
    name_eng: str
    name_th: str
    api_url: str
    param1: str