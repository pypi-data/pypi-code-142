from os import getenv

from ocrd_utils import initLogging, getLogger

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

SERVER_URL: str = getenv("OCRD_WEBAPI_SERVER_PATH", "http://localhost:8000")

app = FastAPI(
    title="OCR-D Web API",
    description="HTTP API for offering OCR-D processing",
    contact={"email": "test@example.com"},
    license={
        "name": "Apache 2.0",
        "url": "http://www.apache.org/licenses/LICENSE-2.0.html",
    },
    version="0.0.1",
    servers=[
        {
            "url": SERVER_URL,
            "description": "The URL of your server offering the OCR-D API.",
        }
    ],
)

initLogging()
log = getLogger('ocrd_webapi.main')


@app.exception_handler(Exception)
async def exception_handler_empty404(request: Request, exc: Exception):
    """
    Exception-Handler needed to return Empty 404 JSON response
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={} if not exc.body else exc.body)


@app.on_event("startup")
async def on_startup():
    log.info("Starting up")


@app.on_event("shutdown")
async def on_shutdown():
    log.info("Shutting down")


@app.get("/")
async def test():
    """
    to test if server is running on root-path
    """
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
