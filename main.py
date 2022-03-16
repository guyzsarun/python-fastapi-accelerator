import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return {"Hello": "World2"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)