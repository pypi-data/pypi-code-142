import logging

from fastapi.testclient import TestClient

from tpds.api.api.schemas.hw import DeviceConnectDetails

LOGGER = logging.getLogger(__name__)


def test_ecc608_connect(client: TestClient) -> None:
    data = DeviceConnectDetails(name="ATECC608", address=0x6C)
    connect_response = client.post("/device/connect", json=data.dict())
    assert connect_response.status_code == 200
    status = connect_response.json()["status"]
    description = connect_response.json()["description"]
    LOGGER.info(f"""\nConnection Status:{status} Description:{description}""")
    assert status == 0, description

    data = DeviceConnectDetails(name="ATECC608", address=0x6A)
    connect_response = client.post("/device/connect", json=data.dict())
    assert connect_response.status_code == 200
    status = connect_response.json()["status"]
    description = connect_response.json()["description"]
    LOGGER.info(f"""\nConnection Status:{status} Description:{description}""")
    assert status == 0, description

    data = DeviceConnectDetails(name="ATECC608", address=0xC0)
    connect_response = client.post("/device/connect", json=data.dict())
    assert connect_response.status_code == 200
    status = connect_response.json()["status"]
    description = connect_response.json()["description"]
    LOGGER.info(f"""\nConnection Status:{status} Description:{description}""")
    assert status == 0, description


def test_ta100_connect(client: TestClient) -> None:
    data = DeviceConnectDetails(name="TA100", address=0x2E)
    connect_response = client.post("/device/connect", json=data.dict())
    assert connect_response.status_code == 200
    status = connect_response.json()["status"]
    description = connect_response.json()["description"]
    LOGGER.info(f"""\nConnection Status:{status} Description:{description}""")
    # assert status == 0, description

    data = DeviceConnectDetails(name="TA100", interface="spi")
    connect_response = client.post("/device/connect", json=data.dict())
    assert connect_response.status_code == 200
    status = connect_response.json()["status"]
    description = connect_response.json()["description"]
    LOGGER.info(f"""\nConnection Status:{status} Description:{description}""")
    # assert status == 0, description
