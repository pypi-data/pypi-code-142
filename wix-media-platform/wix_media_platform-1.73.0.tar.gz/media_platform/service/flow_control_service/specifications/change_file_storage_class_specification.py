from __future__ import annotations

from media_platform.job.specification import Specification
from media_platform.service.file_descriptor import FileStorageClass


class ChangeFileStorageClassSpecification(Specification):
    def __init__(self, storage_class: FileStorageClass):
        self.storage_class = storage_class

    def serialize(self) -> dict:
        return {
            'storageClass': self.storage_class
        }

    @classmethod
    def deserialize(cls, data: dict) -> ChangeFileStorageClassSpecification:
        return cls(data['storageClass'])
