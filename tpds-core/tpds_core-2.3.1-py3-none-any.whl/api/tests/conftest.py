from typing import Generator

import pytest
from fastapi.testclient import TestClient

from ..core import api_inst


@pytest.fixture
def client() -> Generator:
    with TestClient(api_inst) as c:
        yield c
