import logging
import time
from pathlib import Path
from typing import BinaryIO, Dict, Mapping, Optional

import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout
from requests.models import Response

from kognic.base_clients.cloud_storage.upload_spec import UploadSpec, UploadableData
from kognic.base_clients.util import RETRYABLE_STATUS_CODES, get_wait_time

log = logging.getLogger(__name__)


class UploadHandler:

    def __init__(self, max_retry_attempts: int = 23, max_retry_wait_time: int = 60, timeout: int = 60) -> None:
        """
        :param max_upload_retry_attempts: Max number of attempts to retry uploading a file to GCS.
        :param max_upload_retry_wait_time:  Max with time before retrying an upload to GCS.
        :param timeout: Max time to wait for response from server.
        """
        self.max_num_retries = max_retry_attempts
        self.max_retry_wait_time = max_retry_wait_time  # seconds
        self.timeout = timeout  # seconds

    #  Using similar retry strategy as gsutil
    #  https://cloud.google.com/storage/docs/gsutil/addlhelp/RetryHandlingStrategy
    def _upload_file(self, upload_url: str, file: UploadableData, headers: Dict[str, str], number_of_retries: int) -> None:
        """
        Upload the file to GCS, retries if the upload fails with some specific status codes or timeouts.
        """
        try:
            resp = requests.put(upload_url, data=file, headers=headers, timeout=self.timeout)
            resp.raise_for_status()
        except Timeout as t:
            if number_of_retries > 0:
                self._handle_network_timeout(number_of_retries)
                self._upload_file(upload_url, file, headers, number_of_retries - 1)
            else:
                raise t
        except (HTTPError, ConnectionError) as e:
            http_condition = number_of_retries > 0 and resp.status_code in RETRYABLE_STATUS_CODES
            if http_condition or isinstance(e, ConnectionError):
                self._handle_upload_error(resp, number_of_retries)
                self._upload_file(upload_url, file, headers, number_of_retries - 1)
            else:
                raise e

    def _handle_network_timeout(self, number_of_retries: int):
        upload_attempt = self.max_num_retries - number_of_retries + 1
        wait_time = get_wait_time(upload_attempt, self.max_retry_wait_time)
        log.warning(
            f"Failed to upload file. Network timeout"
            f"Attempt {upload_attempt}/{self.max_num_retries}, retrying in {int(wait_time)} seconds."
        )
        time.sleep(wait_time)

    def _handle_upload_error(self, resp: Response, number_of_retries: int):
        upload_attempt = self.max_num_retries - number_of_retries + 1
        wait_time = get_wait_time(upload_attempt, self.max_retry_wait_time)
        log.error(
            f"Failed to upload file. Got response: {resp.status_code}: {resp.content}"
            f"Attempt {upload_attempt}/{self.max_num_retries}, retrying in {int(wait_time)} seconds."
        )
        time.sleep(wait_time)

    def upload_files(self, upload_specs: Mapping[str, UploadSpec]) -> None:
        """
        Upload all files to cloud storage

        :param upload_specs: map between filename and details of what to upload where
        """
        for (resource_id, upload_spec) in upload_specs.items():
            if not upload_spec.data and not upload_spec.callback:
                self._upload_from_local_file(upload_spec)
            elif upload_spec.data:
                self._upload_from_blob(upload_spec)
            elif upload_spec.callback:
                self._upload_from_callback(upload_spec)

    def upload_file(self, file: BinaryIO, url: str) -> None:
        headers = {"Content-Type": "application/json"}
        self._upload_file(url, file, headers, self.max_num_retries)

    def _upload(self, upload_spec: UploadSpec, data: UploadableData):
        headers = {"Content-Type": upload_spec.content_type}
        self._upload_file(upload_spec.destination, data, headers, self.max_num_retries)

    def _upload_from_blob(self, upload_spec: UploadSpec):
        log.debug(f"Blob upload for filename={upload_spec.filename}")
        self._upload(upload_spec, upload_spec.data)

    def _upload_from_local_file(self, upload_spec: UploadSpec):
        log.debug(f"Upload from local file for filename={upload_spec.filename}")
        file = Path(upload_spec.filename).expanduser().open('rb')
        self._upload(upload_spec, file)

    def _upload_from_callback(self, upload_spec: UploadSpec):
        log.debug(f"Upload from callback for filename={upload_spec.filename}")
        try:
            data = upload_spec.callback(upload_spec.filename)
            self._upload(upload_spec, data)
        except Exception as e:
            raise Exception("Failed to upload file: callback failed", e)
        pass
