from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import requests
import pandas as pd
import ApiUrl

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def result(res):
    return {"result":res}

@app.get("/")
async def main():
    return 'Hello World'

@app.get("/List")
async def List():
    response = requests.get(ApiUrl.List).json()
    return response

@app.post("/ApiSignUp")
async def ApiSignUp(name_eng : str, name_th : str, api_url : str, param1 : str):
    request = requests.post(url = ApiUrl.Signup, data={'name_eng' : name_eng, 'name_th' : name_th, 'api_url' : api_url, 'param1' : param1})
    code = request.status_code
    reason = request.reason
    status = {'code' : code,'reason' : reason}
    return status


if __name__ == '__main__':
   uvicorn.run(app, host="0.0.0.0", port=80, debug=True)