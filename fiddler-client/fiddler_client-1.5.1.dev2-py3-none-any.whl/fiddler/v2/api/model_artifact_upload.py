import math
import os
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Callable, Dict, List

from fiddler.libs.http_client import RequestClient
from fiddler.utils import logging
from fiddler.v2.constants import CONTENT_TYPE_OCTET_STREAM_HEADER, MULTI_PART_CHUNK_SIZE
from fiddler.v2.utils.response_handler import APIResponseHandler

logger = logging.getLogger(__name__)


class _AbstractModelUploader(ABC):
    """Abstract class for uploading model artifact"""

    def __init__(
        self,
        client: RequestClient,
        model_name: str,
        project_name: str,
        organization_name: str,
        update: bool = False,
    ) -> None:
        """
        Abstract class for uploading model artifact
        :param client: HTTP client
        :param model_name: Model name
        :param project_name: Project name
        :param organization_name: Organization name
        :param update: Set True for updating artifact, False for adding artifact
        """
        self.client = client
        self.model_name = model_name
        self.project_name = project_name
        self.organization_name = organization_name
        self.update = update

    @abstractmethod
    def upload(self, file_path: Path) -> str:
        pass

    def _get_method(self) -> Callable:
        """Get HTTP method"""
        return self.client.put if self.update else self.client.post


class MultiPartModelUploader(_AbstractModelUploader):
    """Upload model artifact with multi-part upload"""

    INITIALIZE_URL = 'model-artifacts/multi-part-upload/initialize'
    UPLOAD_URL = 'model-artifacts/multi-part-upload/upload'
    COMPLETE_URL = 'model-artifacts/multi-part-upload/complete'

    def _initialize_multi_part_upload(self) -> str:
        """
        Initialize multi-part upload request
        :return: Multi-part upload id
        """
        logger.info(
            'Model[%s/%s] - Initializing multi-part model upload',
            self.project_name,
            self.model_name,
        )

        method = self._get_method()

        response = method(
            url=self.INITIALIZE_URL,
            data={
                'model_name': self.model_name,
                'project_name': self.project_name,
                'organization_name': self.organization_name,
            },
        )

        response_data = APIResponseHandler(response).get_data()

        logger.info(
            'Model[%s/%s] - Multi-part model upload initialized',
            self.project_name,
            self.model_name,
        )
        return response_data.get('upload_id')

    def _upload_multi_part_chunk(
        self, data: bytes, upload_id: str, part_number: int
    ) -> Dict:
        """
        Upload data chunk
        :param data: Data chunk
        :param upload_id: Multi-part upload id
        :param part_number: Chunk part number
        :return: Part details
        """
        method = self._get_method()

        response = method(
            url=self.UPLOAD_URL,
            params={
                'model_name': self.model_name,
                'project_name': self.project_name,
                'organization_name': self.organization_name,
                'upload_id': upload_id,
                'part_number': part_number,
            },
            data=data,
            headers=CONTENT_TYPE_OCTET_STREAM_HEADER,
        )
        response_data = APIResponseHandler(response).get_data()

        return {
            'etag': response_data.get('etag'),
            'part_number': response_data.get('part_number'),
        }

    def _complete_multi_part_upload(
        self,
        upload_id: str,
        parts: List[Dict],
    ) -> str:
        """
        Complete multi-part upload request
        :param upload_id: Multi-part upload id
        :param parts: List of all parts
        :return: Async job uuid
        """
        method = self._get_method()
        response = method(
            url=self.COMPLETE_URL,
            data={
                'model_name': self.model_name,
                'project_name': self.project_name,
                'organization_name': self.organization_name,
                'upload_id': upload_id,
                'parts': parts,
            },
        )

        logger.info(
            'Model[%s/%s] - Multi-part model upload completed',
            self.project_name,
            self.model_name,
        )
        data = APIResponseHandler(response).get_data()
        return data['job_uuid']

    def upload(self, file_path: Path) -> str:
        """
        Upload model artifact
        :param file_path: Path to model artifact tar file
        :return: Async job uuid
        """
        # 1. Initialize multi-part upload request
        upload_id = self._initialize_multi_part_upload()
        part_number = 1
        parts = []
        file_size = os.path.getsize(file_path)
        total_chunks = math.ceil(file_size / MULTI_PART_CHUNK_SIZE)

        # 2. Chunk and upload
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(MULTI_PART_CHUNK_SIZE)
                if not data:
                    break

                logger.info(
                    'Model[%s/%s] - Uploading multi-part chunk - %d/%d',
                    self.project_name,
                    self.model_name,
                    part_number,
                    total_chunks,
                )

                part = self._upload_multi_part_chunk(
                    data=data,
                    upload_id=upload_id,
                    part_number=part_number,
                )
                parts.append(part)
                logger.info(
                    'Model[%s/%s] - Uploaded multi-part chunk - %d/%d',
                    self.project_name,
                    self.model_name,
                    part_number,
                    total_chunks,
                )
                part_number += 1

        # 3: Complete the upload
        return self._complete_multi_part_upload(
            upload_id=upload_id,
            parts=parts,
        )


class ModelUploader(_AbstractModelUploader):
    """Upload model artifact in a single request"""

    UPLOAD_URL = 'model-artifacts/upload'

    def upload(self, file_path: Path) -> str:
        """
        Upload model artifact
        :param file_path: Path to model artifact tar file
        :return: Async job uuid
        """
        logger.info(
            'Model[%s/%s] - Uploading model artifact',
            self.project_name,
            self.model_name,
        )

        method = self._get_method()

        with open(file_path, 'rb') as f:
            data = f.read()
            response = method(
                url=self.UPLOAD_URL,
                params={
                    'model_name': self.model_name,
                    'project_name': self.project_name,
                    'organization_name': self.organization_name,
                },
                data=data,
                headers=CONTENT_TYPE_OCTET_STREAM_HEADER,
            )

        logger.info(
            'Model[%s/%s] - Uploaded model artifact',
            self.project_name,
            self.model_name,
        )

        data = APIResponseHandler(response).get_data()
        return data['job_uuid']
