from enum import StrEnum

from esetconnect.urls.base import Base


class Detections(StrEnum):
    GET_DETECTIONS = f"{Base.BASE_URL}/detections"
