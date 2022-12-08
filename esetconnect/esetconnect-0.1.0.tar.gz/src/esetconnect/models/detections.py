from datetime import datetime
from enum import StrEnum
from typing import Optional

import pydantic


class Category(StrEnum):
    UNSPECIFIED = "DETECTION_CATEGORY_UNSPECIFIED"
    CORRELATION_RULE = "DETECTION_CATEGORY_CORRELATION_RULE"
    FIREWALL_RULE = "DETECTION_CATEGORY_FIREWALL_RULE"
    ANTIVIRUS = "DETECTION_CATEGORY_ANTIVIRUS"
    HIPS = "DETECTION_CATEGORY_HIPS"
    NETWORK_INTRUSION = "DETECTION_CATEGORY_NETWORK_INTRUSION"
    HIPS_RULE = "DETECTION_CATEGORY_HIPS_RULE"
    WEB_ACCESS = "DETECTION_CATEGORY_WEB_ACCESS"
    VULNERABILITY = "DETECTION_CATEGORY_VULNERABILITY"
    APPLICATION_PATCH = "DETECTION_CATEGORY_APPLICATION_PATCH"


class CommunicationDirection(StrEnum):
    UNSPECIFIED = "NETWORK_COMMUNICATION_DIRECTION_UNSPECIFIED"
    INBOUND = "NETWORK_COMMUNICATION_DIRECTION_INBOUND"
    OUTBOUND = "NETWORK_COMMUNICATION_DIRECTION_OUTBOUND"


class Process(pydantic.BaseModel):
    path: str


class Context(pydantic.BaseModel):
    circumstances: str
    device_uuid: str
    process: Process
    user_name: str


class NetworkCommunication(pydantic.BaseModel):
    direction: CommunicationDirection
    local_ip_address: str
    local_port: int
    procotol_name: str
    remote_ip_address: str
    remote_port: int


class Response(pydantic.BaseModel):
    description: Optional[str]
    device_restart_required: Optional[bool]
    display_name: Optional[str]
    protection_name: Optional[str]


class SeverityLevel(StrEnum):
    UNSPECIFIED = "SEVERITY_LEVEL_UNSPECIFIED"
    DIAGNOSTIC = "SEVERITY_LEVEL_DIAGNOSTIC"
    INFORMATIONAL = "SEVERITY_LEVEL_INFORMATIONAL"
    LOW = "SEVERITY_LEVEL_LOW"
    MEDIUM = "SEVERITY_LEVEL_MEDIUM"
    HIGH = "SEVERITY_LEVEL_HIGH"


class Detection(pydantic.BaseModel):
    category: Category
    context: Context
    display_name: str
    network_communication: Optional[NetworkCommunication]
    object_hash_sha1: str
    object_name: str
    object_type_name: str
    object_url: str
    occur_time: datetime
    responses: Response
    severity_level: SeverityLevel
    type_name: str
    uuid: str


class GetDetectionsParams(pydantic.BaseModel):
    device_uuid: Optional[str]
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    page_size: Optional[int]
    page_token: Optional[str]


class GetDetectionsResponse(pydantic.BaseModel):
    detections: list[Detection]
    next_page_token: str
    total_size: int
