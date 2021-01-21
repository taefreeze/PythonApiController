from requests.models import Response
from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import requests
import pandas as pd
import ApiUrl
import model as Model
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


@app.get("/ListOld")
async def ListOld():
    response = requests.get(ApiUrl.ListThun).json()
    return response

@app.get("/ApiList")
async def ApiList(page : int=1):
    data = {
        'page' : page,
        'limit' : 10
    }
    request = requests.get(url=ApiUrl.ListPage, params=data)
    return request.json()

@app.post("/ApiSignUpOld")
async def ApiSignUpOld(name_eng: str, name_th: str, api_url: str, param1: str):
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


@app.post("/ApiSignUp")
async def ApiSignUp(Registers : Model.ServiceRegisterModel):
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
async def User(Userinfo : Model.UserInfoModel):
    data = {
        'fullname' : Userinfo.Name,
        'id_token' : Userinfo.Token,
        'google_photo' : Userinfo.Image,
        'gmail' : Userinfo.Email   
        }
    request = requests.post(url = ApiUrl.User,json=data)
    response = request.json()
    status = {'status' : {'code' : request.status_code, 'reason' : request.reason}}
    return response,status

@app.patch("/Update")
async def Update(Updates : Model.ServiceUpdateModel):
    data = {
            'service_id' : Updates.service_id,
            'service_name' : Updates.service_name,
            'api_url' : Updates.api_url, 
            'permission' : Updates.permission, 
            'user_id' : Updates.user_id
            }
    request = requests.put(url = ApiUrl.Update,json=data)
    response = request.json()
    status = {'status' : {'code' : request.status_code, 'reason' : request.reason}}
    return response,status

@app.delete("/Delete")
async def Delete( Deletes : Model.ServiceDeleteModel):
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
