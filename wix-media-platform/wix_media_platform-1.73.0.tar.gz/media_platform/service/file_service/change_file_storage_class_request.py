from __future__ import annotations

from typing import Dict

from media_platform.http_client.authenticated_http_client import AuthenticatedHTTPClient
from media_platform.service.file_descriptor import FileDescriptor, FileStorageClass
from media_platform.service.media_platform_request import MediaPlatformRequest


class ChangeFileStorageClassRequest(MediaPlatformRequest):
    def __init__(self, authenticated_http_client: AuthenticatedHTTPClient, base_url: str):
        super().__init__(authenticated_http_client, 'PUT', base_url + '/files/storage_class', FileDescriptor)

        self.file_id = None
        self.path = None
        self.storage_class = None

    def set_path(self, path: str) -> ChangeFileStorageClassRequest:
        self.path = path
        return self

    def set_id(self, file_id: str) -> ChangeFileStorageClassRequest:
        self.file_id = file_id
        return self

    def set_storage_class(self, storage_class: FileStorageClass) -> ChangeFileStorageClassRequest:
        self.storage_class = storage_class
        return self

    def execute(self) -> FileDescriptor:
        return super().execute()

    def validate(self):
        FileDescriptor.storage_class_validator(self.storage_class)

        if self.path is not None:
            FileDescriptor.path_validator(self.path)

        if not self.path and not self.file_id:
            raise ValueError('must provide path or id')

    def _params(self) -> Dict:
        return {
            'id': self.file_id,
            'path': self.path,
            'storageClass': self.storage_class,
        }
