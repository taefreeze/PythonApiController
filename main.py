from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import requests
import pandas as pd

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
    response = requests.get("https://taeapiplatform.herokuapp.com/ApiList").json()
    return response

@app.post("ApiSignUp")
async def ApiSignUp(name_eng : str, name_th : str, api_url : str, param1 : str):
    API_ENDPOINT = "https://taeapiplatform.herokuapp.com/ApiSignup/"
    response = requests.post(url = API_ENDPOINT, data={'name_eng' : name_eng, 'name_th' : name_th, 'api_url' : api_url, 'param1' : param1})
    code = response.status_code
    reason = response.reason
    return code

if __name__ == '__main__':
   uvicorn.run(app, host="0.0.0.0", port=80, debug=True)