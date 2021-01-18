from requests.models import Response
from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import requests
import pandas as pd
import ApiUrl
from model import ServiceRegisterModel,ServiceDeleteModel,UserInfoModel
import json
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def result(res):
    return {"result": res}


@app.get("/")
async def main():
    return 'Hello World'


@app.get("/List")
async def List():
    response = requests.get(ApiUrl.ListThun).json()
    return response


@app.post("/ApiSignUp")
async def ApiSignUp(name_eng: str, name_th: str, api_url: str, param1: str):
    data = {
        'name_eng': name_eng,
        'name_th': name_th,
        'api_url': api_url,
        'param1': param1
    }
    request = requests.post(url=ApiUrl.SignupThun, json=data)
    response = request.json()
    status = {'status': {'code': request.status_code, 'reason': request.reason}}
    return response, status


@app.post("/ApiSignUpJson")

async def ApiSignUpJson(Registers : ServiceRegisterModel):
    data = {
            'service_name' : Registers.service_name,
            'api_url' : Registers.api_url, 
            'permission' : Registers.permission, 
            'user_id' : Registers.user_id
            }
    request = requests.post(url = ApiUrl.SignupThun, json=data)
    response = request.json()
    status = {'status': {'code': request.status_code, 'reason': request.reason}}
    return response, status


@app.post("/User")
async def User(Userinfo : UserInfoModel):
    data = {
        'Name' : Userinfo.EW,
        'Fullname' : Userinfo.Ed,
        'Lastname' : Userinfo.IU,
        'google_id' : Userinfo.aV,
        'user_photo' : Userinfo.fL,
        'email' : Userinfo.uu   
        }
    request = requests.post(url = ApiUrl.User,json=data)
    response = request.json()
    status = {'status' : {'code' : request.status_code, 'reason' : request.reason}}
    return response,status

@app.post("/Update")
async def Update(id: int, data: dict):
    return 0


@app.delete("/Delete")
async def Delete( Deletes : ServiceDeleteModel):
    data = {
        'service_id' : Deletes.service_id,
        'user_id' : Deletes.user_id
    }
    delete = requests.delete(url= ApiUrl.Delete, json=data)
    response = delete.json()
    status = {'status' :{'code' : delete.status_code,'reason' : delete.reason}}
    return response,status



if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=80, debug=True)
