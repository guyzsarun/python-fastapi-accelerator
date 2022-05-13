import uvicorn
from fastapi import FastAPI
import os


app = FastAPI()


@app.get("/")
def hello_world():
    return {"Hello": "World"}


@app.get("/ping")
def ping():
    return "pong"


@app.get("/status")
def status():
    env = os.environ
    return {
        "HOSTNAME": env.get("HOSTNAME"),
        "K_REVISION": env.get("K_REVISION"),
        "PORT": env.get("PORT"),
        "K_CONFIGURATION": env.get("K_CONFIGURATION"),
    }


if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8080)
