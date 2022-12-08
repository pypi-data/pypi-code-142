import os
import sys
from pathlib import Path

import uvicorn
from dotenv import load_dotenv
from errors.http_error import http_error_handler, validation_exception_handler
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from loguru import logger
from routers.router import router as api_router
from starlette.middleware.cors import CORSMiddleware


sys.path.append(Path(__file__).parent.absolute().as_posix())

dotenv_path = "api/.env"
load_dotenv(dotenv_path)
api_host = os.environ.get("API_HOST")
api_port = os.environ.get("API_PORT")


def get_app() -> FastAPI:
    app = FastAPI(title="Domain Classification API", debug=True, version="v.01")
    # This middleware enables allow all cross-domain requests to the API from a browser.
    # For production deployments, it could be made more restrictive.
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_exception_handler(HTTPException, http_error_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)

    app.include_router(api_router)

    return app


app = get_app()


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down API")


if __name__ == "__main__":
    uvicorn.run(app, host=api_host, port=int(api_port))
