import json
from enum import Enum
from typing import Optional

from .messaging import IcatMessagingClient


class StatusType(Enum):
    ARCHIVING = "archiving"
    RESTORATION = "restoration"


class StatusLevel(Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"


class IcatArchiveStatusClient:
    """Client for storing archive and restoration status in ICAT."""

    def __init__(
        self,
        queue_urls: list,
        queue_name: str = "icatArchiveRestoreStatus",
        monitor_port: Optional[int] = None,
        timeout: Optional[float] = None,
    ):
        self._client = IcatMessagingClient(
            queue_urls, queue_name, monitor_port=monitor_port, timeout=timeout
        )

    def send_archive_status(
        self, dataset_id: int, type: StatusType, level: StatusLevel, message: str
    ):
        assert dataset_id, "ICAT requires the datasetId"
        assert type, "ICAT requires the type"
        assert level, "ICAT requires the level"
        root = {
            "datasetId": dataset_id,
            "type": type.value,
            "level": level.value,
            "message": message,
        }
        data = json.dumps(root).encode("utf-8")
        self._client.send(data)

    def check_health(self):
        """Raises an exception when not healthy"""
        self._client.check_health()
