import json
from typing import List, Dict, Union
from urllib.parse import urlencode
from pydantic import Field, BaseModel as BaseLintModel


class LintModel(BaseLintModel):
    class Config:
        arbitrary_types_allowed = True


class RequestContainer(LintModel):
    queries: Dict[str, List] = Field(default_factory=dict)
    headers: Dict[str, str]
    body_in_byte: bytes = b''

    @property
    def string_body(self) -> str:
        return self.body_in_byte.decode('utf-8')

    @property
    def json_body(self) -> Union[dict, list, None]:
        try:
            return json.loads(self.body_in_byte.decode('utf-8'))
        except json.JSONDecodeError:
            return None

    def to_dict(self) -> Dict:
        return {
            'queries': self.queries,
            'headers': {k: v for k, v in self.headers.items()},
            'data': self.string_body,
        }


class ResponseContainer(LintModel):
    headers: Dict[str, str]
    body_in_byte: bytes = b''

    @property
    def string_body(self) -> str:
        return self.body_in_byte.decode('utf-8')

    @property
    def json_body(self) -> Union[dict, list, None]:
        try:
            return json.loads(self.body_in_byte.decode('utf-8'))
        except json.JSONDecodeError:
            return None

    def to_dict(self) -> Dict:
        return {
            'headers': {k: v for k, v in self.headers.items()},
            'data': self.string_body,
        }


class RequestRecord(LintModel):
    request_id: str
    protocol: str  # either “http” or “https”
    method: str
    host: str
    path: str
    uri: str
    remote_ip: str
    http_version: str
    status_code: int
    reason: str
    time_elapsed: str = None
    request: RequestContainer = None
    response: ResponseContainer = None

    @property
    def request_raw(self) -> str:
        uri = f'{self.method} {self.path}?{urlencode(self.request.queries, doseq=True)} {self.http_version}'
        headers = '\n'.join([f'{k}: {v}' for k, v in self.request.headers.items()])
        body = self.request.string_body
        return '\n'.join([uri, headers, '\n', body])

    @property
    def response_raw(self) -> str:
        uri = f'{self.http_version} {self.status_code} {self.reason}'
        headers = '\n'.join([f'{k}: {v}' for k, v in self.response.headers.items()])
        body = self.response.string_body
        return '\n'.join([uri, headers, '\n', body])

    def to_dict(self):
        d = super(RequestRecord, self).dict()
        d.update({
            'request': self.request.to_dict() if self.request else None,
            'response': self.response.to_dict() if self.response else None,
        })
        return d
