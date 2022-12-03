from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn


def start_api():
    app = FastAPI()
    app.mount("/api", StaticFiles(directory="tileset_analyzer/static/data"), name="api")
    app.mount("/", StaticFiles(directory="tileset_analyzer/static/ui", html=True), name="ui")
    
    uvicorn.run(app, host="0.0.0.0", port=8080)
    
