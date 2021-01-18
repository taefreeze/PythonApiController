from pydantic import BaseModel
from typing import Optional
import requests
from fastapi import Request, FastAPI
from typing import Optional


class ServiceRegisterModel(BaseModel):
    service_name    : str
    api_url         : str
    permission      : str
    user_id         : str

class UserInfoModel(BaseModel):
    EW  : str
    Ed  : str
    IU  : str
    aV  : str
    fL  : str
    uu  : str

class ServiceDeleteModel(BaseModel):
    service_id  : str
    user_id     : str