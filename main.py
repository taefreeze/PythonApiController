from os import stat_result
from requests.api import request
from requests.models import Response
from fastapi import FastAPI
from starlette import responses
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import requests
import pandas as pd
import ApiUrl
import model as Model
import json
from pydantic import BaseModel
from typing import List, Optional
from fastapi.encoders import jsonable_encoder


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


@app.get("/service/list")
async def serviceList(page : int):
    data = {
        'page' : page,
        'limit' : 10
    }
    request = requests.get(url=ApiUrl.ListPage, params=data)
    return request.json()


@app.post("/service/add")
async def serviceAdd(Registers : Model.ServiceRegisterModel):
    data = {
            'service_name' : Registers.service_name,
            'api_url' : Registers.api_url, 
            'permission' : Registers.permission, 
            'user_id' : Registers.user_id,
            'description' : Registers.description
            }
    request = requests.post(url = ApiUrl.Signup, json=data)
    response = request.json()
    status = {'status': {'code': request.status_code, 'reason': request.reason}}
    return response, status


@app.patch("/service/update")
async def serviceUpdate(Updates : Model.ServiceUpdateModel):
    data = {
            'service_id' : Updates.service_id,
            'service_name' : Updates.service_name,
            'api_url' : Updates.api_url, 
            'permission' : Updates.permission, 
            'user_id' : Updates.user_id,
            'description' : Updates.description
            }
    request = requests.patch(url = ApiUrl.Update,json=data)
    response = request.json()
    status = {'status' : {'code' : request.status_code, 'reason' : request.reason}}
    return response,status


@app.delete("/service/delete")
async def serviceDelete( Deletes : Model.ServiceDeleteModel):
    data = {
        'service_id' : Deletes.service_id,
        'user_id' : Deletes.user_id
    }
    delete = requests.delete(url= ApiUrl.Delete, json=data)
    response = delete.json()
    status = {'status' :{'code' : delete.status_code,'reason' : delete.reason}}
    return response,status


@app.get("/administrator")
async def admin(page: int, user_id: str, status: str):
    data = {
        'page' : page,
        'limit' : 10,
        'user_id' : user_id,
        'status' : status
    }
    request = requests.get(url= ApiUrl.admins,params= data)
    response = request.json()
    status = {'status' :{'code' : request.status_code,'reason' : request.reason}}
    return response,status


@app.get("/user/service")
async def userService(page: int, user_id: str):
    data = {
        'page' : page,
        'user_id' : user_id,
        'limit' : 10
    }
    request = requests.get(url=ApiUrl.userService, params = data)
    return request.json()


@app.post("/user/login")
async def login(Userinfo : Model.UserInfoModel):
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


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=80, debug=True)
