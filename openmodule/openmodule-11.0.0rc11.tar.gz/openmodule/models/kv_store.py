from typing import Optional, List, Dict

from openmodule.models.base import OpenModuleModel


class KVSetRequestKV(OpenModuleModel):
    key: str
    value: str = "null"
    e_tag: Optional[int]
    previous_e_tag: Optional[int]


class KVSetRequest(OpenModuleModel):
    service: str
    kvs: List[KVSetRequestKV]


class KVSetResponseKV(OpenModuleModel):
    key: str
    status: str = "error"
    error: Optional[str]


class KVSetResponse(OpenModuleModel):
    kvs: List[KVSetResponseKV] = []


class KVSyncRequest(OpenModuleModel):
    service: str
    kvs: Dict[str, Optional[int]]


class KVSyncResponse(OpenModuleModel):
    additions: Dict[str, Optional[int]]
    changes: Dict[str, Optional[int]]
    missing: Dict[str, Optional[int]]


class ServerSyncResponseKV(OpenModuleModel):
    key: str
    status: str
    error: Optional[str]


class ServerSyncResponse(OpenModuleModel):
    successes: List[ServerSyncResponseKV]
    errors: List[ServerSyncResponseKV]
