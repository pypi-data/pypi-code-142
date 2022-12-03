from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn


def start_api():
    app = FastAPI()
    app.mount("/", StaticFiles(directory="ui", html=True), name="static")
    uvicorn.run(app, host="0.0.0.0", port=8080)
    
