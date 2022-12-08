import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from fastapi.middleware.cors import CORSMiddleware
from be.errors.exceptions import ApiException
from be.errors.handlers import (
    api_exception_handler,
    regular_exception_handler,
    validation_exception_handler,
)
from be.questions.endpoints import router as questions_router
from be.sessions.endpoints import router as session_endpoints

app = FastAPI()

app.include_router(questions_router)
app.include_router(session_endpoints)

app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(ApiException, api_exception_handler)
app.add_exception_handler(Exception, regular_exception_handler)

# TODO: this should not be hardcoded
# TODO: security concerns?
origins = [
    "http://localhost",
    "http://localhost:8081",
    "http://20.199.181.88"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, host="0.0.0.0")
