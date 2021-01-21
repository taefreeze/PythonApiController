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


class ServiceUpdateModel(BaseModel):
    service_id: str
    service_name: str
    api_url: str
    permission: str
    user_id: str


class UserInfoModel(BaseModel):
    Name: str
    Email: str
    Image: str
    Token: str


class ServiceDeleteModel(BaseModel):
    service_id: str
    user_id: str
