import os

import pytest

from authelio_sdk.client import Client
from authelio_sdk.config import Config

AUTHELIO_API_KEY = os.environ['AUTHELIO_API_KEY']
AUTHELIO_API_SECRET = os.environ['AUTHELIO_API_SECRET']
AUTHELIO_API_URL = os.environ.get('AUTHELIO_API_URL')

assert AUTHELIO_API_KEY is not None
assert len(AUTHELIO_API_KEY)

assert AUTHELIO_API_SECRET is not None
assert len(AUTHELIO_API_SECRET)


@pytest.fixture(scope='session')
def sdk_client() -> Client:
    config = Config(public_api_url=AUTHELIO_API_URL) if AUTHELIO_API_URL else None

    return Client(
        api_key=AUTHELIO_API_KEY,
        api_secret=AUTHELIO_API_SECRET,
        config=config
    )
