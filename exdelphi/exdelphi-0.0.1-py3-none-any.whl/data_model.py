from pydantic import BaseModel
from api_time import int_to_datetime


class Data(BaseModel):
    t: int
    v: float


class User(BaseModel):
    id: int


class Token(BaseModel):
    access_token: str
    token_type: str


class Product(BaseModel):
    id: int
    name: str


class Dataset(BaseModel):
    id: int
    start_time: int

    def __repr__(self):
        timestamp: str = str(int_to_datetime(self.start_time))
        return f"Dataset(id={self.id}, start_time={timestamp})"
