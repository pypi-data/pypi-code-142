import logging
import os
from pathlib import Path

from fastapi.testclient import TestClient

from tpds.api.api.schemas.hw import BoardDetails

LOGGER = logging.getLogger(__name__)


def test_boards(client: TestClient) -> None:
    data = BoardDetails()
    boards_response = client.post("/boards/add_details/DM320118", json=data.dict())
    assert boards_response.status_code == 200

    boards_response = client.get("/boards/get_details/DM320118")
    assert boards_response.status_code == 200

    boards_response = client.get("/boards/get_supported")
    assert boards_response.status_code == 200

    boards_response = client.get("/boards/get_factory_programmed")
    assert boards_response.status_code == 200

    boards_response = client.get("/boards/get_connected")
    assert boards_response.status_code == 200

    _test_upload_file = Path(
        os.path.join(
            os.getenv("CONDA_PREFIX"),
            "tpds_core",
            "assets",
            "proto_boards",
            "DM320118",
            "DM320118.hex",
        )
    ).read_bytes()
    _files = {"upload_file": _test_upload_file}
    boards_response = client.post("/boards/program_image/DM320118", files=_files)
    assert boards_response.status_code == 200
    LOGGER.info(boards_response.json())
