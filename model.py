from pydantic import BaseModel
from typing import Optional,List
import requests
from fastapi import Request, FastAPI
from typing import Optional


class RegisterModel(BaseModel):
    service_name: str
    api_url: str
    permission: str
    user_id: str

class ServiceRegisterModel(BaseModel):
    service_name : str
    api_url      : str
    permission   : str
    user_id      : str
    description : Optional[str] = None


class UserInfoModel(BaseModel):
    Name: str
    Email: str
    Image: str
    Token: str


class ServiceDeleteModel(BaseModel):
    service_id: str
    user_id: str
    

class ServiceUpdateModel(BaseModel):
    service_name    : Optional[str] = None
    api_url         : Optional[str] = None
    permission      : Optional[str] = None
    service_id      : str
    user_id         : str 
    description     : Optional[str] = None