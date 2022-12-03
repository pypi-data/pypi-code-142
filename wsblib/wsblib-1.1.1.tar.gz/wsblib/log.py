from datetime import datetime

from http_pyparser import Response
from .request import RequestData


def log_request(response: Response, request: RequestData) -> None:
    time = datetime.now()

    path = request.real_path
    status = response.status
    method = request.method
    host = request.remote_addr[0]

    print(f'[\033[33m{time}\033[m]', end='')
    print(f'[{host}]', end=' ', flush=True)

    if 100 <= status < 200 or 300 <= status < 400:
        print(f'\033[33m{status}\033[m', flush=True, end=' ')
    elif 200 <= status < 300:
        print(f'\033[32m{status}\033[m', flush=True, end=' ')
    elif 400 <= status <= 500:
        print(f'\033[31m{status}\033[m', flush=True, end=' ')

    print(f'{path} ({method})')
