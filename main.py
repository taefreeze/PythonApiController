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
async def ApiSignUp():
    return 0

if __name__ == '__main__':
   uvicorn.run(app, host="0.0.0.0", port=80, debug=True)