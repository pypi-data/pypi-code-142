from enum import Enum
from pathlib import Path
from ssl import SSLContext
from typing import Optional

from icecream import ic
from pydantic import BaseModel, EmailStr, validator


# class EMailSettings(BaseModel):
#     email: EmailStr
#     password: str
#     smtp_server: str
#     smtp_server_port: int
#     keyfile: Optional[str] = None
#     certfile = Optional[str] = None
#     ssl_context: Optional[SSLContext] - None
#     timeout = Optional[int] = None


class EmailListenerSettings(BaseModel):
    email: str
    password: str
    smtp_server: Optional[str]
    smtp_server_port: Optional[int]

