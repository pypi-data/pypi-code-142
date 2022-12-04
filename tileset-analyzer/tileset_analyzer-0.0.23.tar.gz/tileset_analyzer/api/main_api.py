from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
from pathlib import Path

OUTPUT_JSON_PATH = f'{Path(os.path.dirname(__file__)).parent}/static/data'
UI_PATH = f'{Path(os.path.dirname(__file__)).parent}/static/ui'

def start_api():
    app = FastAPI()
    app.mount("/api", StaticFiles(directory=OUTPUT_JSON_PATH), name="api")
    app.mount("/", StaticFiles(directory=UI_PATH, html=True), name="ui")
    
    uvicorn.run(app, host="0.0.0.0", port=8080)
    
