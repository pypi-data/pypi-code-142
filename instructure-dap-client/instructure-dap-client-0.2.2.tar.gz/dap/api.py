import json
import logging
import os
import shutil
import time
from http import HTTPStatus
from typing import Any, List, Optional, Type, TypeVar, Union
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter, Retry
from strong_typing.schema import json_schema_type
from strong_typing.serialization import json_dump_string, json_to_object, object_to_json
import base64
import re

from .dap_error import (
    AuthenticationError,
    NotFoundError,
    OutOfRangeError,
    ProcessingError,
    ServerError,
    ValidationError,
)
from .dap_types import (
    CompleteIncrementalJob,
    CompleteSnapshotJob,
    Credentials,
    IncrementalQuery,
    Job,
    JobID,
    JobStatus,
    Object,
    Query,
    Resource,
    ResourceResult,
    SnapshotQuery,
    TableList,
    TokenProperties,
    VersionedSchema,
)

T = TypeVar("T")


class DAPClientError(RuntimeError):
    pass


class DAPClient:
    _base_url: str
    _api_key: str
    credentials: Credentials
    _session: "DAPSession"

    # 3 retries with delay of [1, 2, 4] seconds
    _retries = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[HTTPStatus.BAD_GATEWAY.value],
    )

    def __init__(
        self, base_url: Optional[str] = None, api_key: Optional[str] = None
    ) -> None:
        base_url_arg = base_url or os.getenv("DAP_API_URL")
        api_key_arg = api_key or os.getenv("DAP_API_KEY")

        if not base_url_arg:
            raise DAPClientError("base URL missing")
        if not api_key_arg:
            raise DAPClientError("API key missing")

        self._base_url = base_url_arg.rstrip("/")
        self._api_key = api_key_arg
        self.credentials = self._decode_api_key(self._api_key)

        logging.info(
            f"Client ID: {self.credentials.client_id}, Client region: {self.credentials.client_region}"
        )

    def __enter__(self):
        session = requests.Session()
        session.mount("https://", HTTPAdapter(max_retries=self._retries))
        self._session = DAPSession(session, self._base_url)
        try:
            logging.info(f"Connecting to {self._base_url}")
            self._session.authenticate(self.credentials)
        except Exception as e:
            logging.error("Failed to authenticate")
            self._session.close()
            self._session = None
            raise
        return self._session

    def _decode_api_key(self, api_key: str) -> Credentials:
        try:
            base64_bytes = api_key.encode("ascii")
            message_bytes = base64.b64decode(base64_bytes)
            decoded_key = message_bytes.decode("ascii")
        except ValueError:
            raise DAPClientError("Failed to decode provided API key.")

        # Decoded API key should match the following pattern: region#client-id:client-token. E.g. us-west-2#123-...-ef2:Abc...K0E
        m = re.match(r"([\w-]+)[#]([\w-]+)[:]", decoded_key)
        if not m:
            raise DAPClientError("Decoded API key does not match the expected pattern.")

        client_id = m.group(2)
        client_region = m.group(1)
        credentials = Credentials(api_key, client_id, client_region)
        return credentials

    def __exit__(self, type, value, traceback):
        self._session.close()
        self._session = None


class DAPSession:
    "Represents an authenticated session to DAP."

    _session: requests.Session

    def __init__(self, session: requests.Session, base_url: str) -> None:
        "Creates a new logical session by encapsulating a network connection."

        self._base_url = base_url
        self._session = session

    def close(self) -> None:
        "Closes the underlying network socket."

        self._session.close()

    def _get(self, path: str, response_type: Type[T]) -> T:
        """
        Sends a request to the server and parses the response into the expected type.

        :param path: The path component of the endpoint to invoke.
        :param response_type: The object type the endpoint returns on success.
        :returns: The object returned on success.
        :raises Exception: The object returned on failure.
        """

        response = self._session.get(f"{self._base_url}{path}")
        return self._process(response, response_type)

    def _map_to_error_type(
        self, response: requests.Response, response_body: Any
    ) -> Union[
        ValidationError,
        NotFoundError,
        OutOfRangeError,
        AuthenticationError,
        ProcessingError,
        ServerError,
    ]:
        "Maps error body and status to Python error object"

        if "error" not in response_body:
            return ServerError(response_body)

        response_body_error = response_body["error"]
        try:
            if (
                response.status_code == HTTPStatus.UNAUTHORIZED.value
                or response.status_code == HTTPStatus.FORBIDDEN.value
            ):
                return json_to_object(AuthenticationError, response_body_error)
            else:
                return json_to_object(
                    Union[
                        ValidationError,
                        NotFoundError,
                        OutOfRangeError,
                        ProcessingError,
                    ],
                    response_body_error,
                )
        except:
            return ServerError(response_body_error)

    def _post(self, path: str, request_data: Any, response_type: Type[T]) -> T:
        """
        Sends a request to the server by serializing a payload object, and parses the response into the expected type.

        :param path: The path component of the endpoint to invoke.
        :param request_data: The object to pass in the request body.
        :param response_type: The object type the endpoint returns on success.
        :returns: The object returned on success.
        :raises Exception: The object returned on failure.
        """

        request_payload = object_to_json(request_data)
        logging.debug(f"POST request payload:\n{repr(request_payload)}")

        response = self._session.post(
            f"{self._base_url}{path}",
            data=json_dump_string(request_payload),
            headers={"Content-Type": "application/json"},
        )
        return self._process(response, response_type)

    def _post_auth_request(self, api_key: str) -> TokenProperties:
        """
        Sends an authentication request to the Identity Service through Instructure API Gateway,
        and parses the response into a TokenProperties object.

        :param api_key: API key to be passed to server.
        :returns: TokenProperties object on success.
        :raises Exception: The object returned on failure.
        """

        response = self._session.post(
            f"{self._base_url}/ids/auth/login",
            data={"grant_type": "client_credentials"},
            headers={"Authorization": "Basic " + api_key},
        )
        return self._process(response, TokenProperties)

    def _process(self, response: requests.Response, response_type: Type[T]) -> T:
        "Extracts an object instance from an HTTP response body."

        try:
            response_payload = response.json()
        except requests.exceptions.JSONDecodeError:
            if response.text:
                logging.error(f"malformed HTTP response:\n{repr(response.text)}")

            raise DAPClientError("malformed HTTP response")

        logging.debug(f"GET/POST response payload:\n{repr(response_payload)}")

        # HTTP status codes between 400 and 600 indicate an error (includes non-standard 5xx server-side error codes)
        if HTTPStatus.BAD_REQUEST.value <= response.status_code <= 600:
            error_object = self._map_to_error_type(response, response_payload)
            logging.warn(f"Received error in response: {error_object}")
            raise error_object
        else:
            response_object = json_to_object(response_type, response_payload)
            return response_object

    def authenticate(self, credentials: Credentials) -> None:
        "Authenticates with API key to receive a JWT."

        logging.info(
            f"Authenticating to DAP in region {credentials.client_region} with Client ID {credentials.client_id}"
        )
        properties = self._post_auth_request(credentials.api_key)
        self._session.headers.update({"x-instauth": f"{properties.access_token}"})

    def query_snapshot(self, namespace: str, table: str, query: SnapshotQuery) -> Job:
        "Start a snapshot query."

        logging.info(f"Query snapshot of table: {table}")
        job = self._post(f"/dap/query/{namespace}/table/{table}/data", query, Job)  # type: ignore
        return job

    def query_incremental(
        self, namespace: str, table: str, query: IncrementalQuery
    ) -> Job:
        "Start an incremental query."

        logging.info(f"Query updates for table: {table}")
        job = self._post(f"/dap/query/{namespace}/table/{table}/data", query, Job)  # type: ignore
        return job

    def get_tables(self, namespace: str) -> List[str]:
        "Get list of tables available for querying."

        logging.info(f"Get list of tables from namespace: {namespace}")
        table_list = self._get(f"/dap/query/{namespace}/table", TableList)
        return table_list.tables

    def get_table_schema(self, namespace: str, table: str) -> VersionedSchema:
        "Get list of tables available for querying."

        logging.info(f"Get schema of table: {table}")
        versioned_schema = self._get(
            f"/dap/query/{namespace}/table/{table}/schema", VersionedSchema
        )
        return versioned_schema

    def download_table_schema(
        self, namespace: str, table: str, output_directory: str
    ) -> None:
        """
        Save schema as a json file into a local directory.

        :param output_directory: Path to the directory to save json file to.
        """

        versioned_schema = self.get_table_schema(namespace, table)
        schema_version = versioned_schema.version
        json_object = object_to_json(versioned_schema)

        os.makedirs(output_directory, exist_ok=True)
        file_name = f"{table}_schema_version_{schema_version}.json"
        file_path = os.path.join(output_directory, file_name)
        with open(file_path, "w") as file:
            json.dump(json_object, file, indent=4)
        logging.info(f"JSON schema downloaded to folder: {output_directory}")

    def get_job(self, job_id: JobID) -> Job:
        "Retrieve job status."

        logging.debug(f"Retrieving job state for job {job_id}")
        job = self._get(f"/dap/job/{job_id}", Job)  # type: ignore
        return job

    def get_job_status(self, job_id: JobID) -> JobStatus:
        "Retrieve job status."

        return self.get_job(job_id).status

    def get_objects(self, job_id: JobID) -> List[Object]:
        "Retrieve object IDs once the query is completed successfully."

        logging.info(f"Retrieving object IDs for job {job_id}")
        job = self._get(f"/dap/job/{job_id}", Job)  # type: ignore
        return job.objects

    def get_resources(self, objects: List[Object]) -> List[Resource]:
        "Retrieve URLs to data stored remotely."

        object_id_list = ", ".join(o.id for o in objects)
        logging.info(f"Retrieve resource URLs for objects: {object_id_list}")
        response = self._post("/dap/object/url", objects, ResourceResult)
        resource_list = [response.urls[resource_id] for resource_id in response.urls]
        return resource_list

    def download_resources(
        self, resources: List[Resource], job_id: JobID, output_directory: str
    ) -> List[str]:
        """
        Save data stored remotely into a local directory.

        :param output_directory: Path to the directory to save downloaded files to.
        :returns: A list of paths to files saved in the local file system.
        """

        local_files: List[str] = []
        dir = os.path.join(output_directory, f"job_{job_id}")
        os.makedirs(dir, exist_ok=True)
        for u in resources:
            url = str(u.url)
            url_path = urlparse(url).path
            file_base_name = os.path.basename(url_path)
            file_path = os.path.join(dir, file_base_name)
            with requests.get(url, stream=True) as data, open(file_path, "wb") as file:
                # save gzip data to file without decompressing
                shutil.copyfileobj(data.raw, file)
            local_files.append(file_path)
        logging.info(f"Files from server downloaded to folder: {dir}")
        return local_files

    def await_job(self, job: Job) -> Job:
        """
        Wait until a job terminates.

        :param job: A job that might be still running.
        :returns: A job that has completed with success or terminated with failure.
        """

        while not job.status.isTerminal():
            delay = 30
            logging.info(
                f"Query job still in status: {job.status.value}. Checking again in {delay} seconds..."
            )
            time.sleep(delay)

            job = self.get_job(job.id)

        logging.info(f"Query job finished with status: {job.status.value}")
        return job

    def execute_job(
        self,
        namespace: str,
        table: str,
        query: Query,
    ) -> Job:
        "Start a query job and wait until it terminates."

        if isinstance(query, SnapshotQuery):
            job = self.query_snapshot(namespace, table, query)
        elif isinstance(query, IncrementalQuery):
            job = self.query_incremental(namespace, table, query)
        else:
            raise TypeError(f"type mismatch for parameter `query`: {type(query)}")

        logging.info(f"Query started with job ID: {job.id}")

        job = self.await_job(job)
        return job

    def fetch_table_data(
        self, namespace: str, table: str, query: Query, output_directory: str
    ) -> List[str]:
        """
        Execute a query job and download data to a local directory.

        :param output_directory: Path to the directory to save downloaded files to.
        :returns: A list of paths to files saved in the local file system.
        """

        # fail early if output directory does not exist and cannot be created
        os.makedirs(output_directory, exist_ok=True)

        job = self.execute_job(namespace, table, query)

        if job.status is JobStatus.Complete:
            if isinstance(job, CompleteSnapshotJob):
                logging.info(
                    f"Data is being queried for the data lake state at {job.at},"
                    + f" with schema version number {job.schema_version}"
                )
            elif isinstance(job, CompleteIncrementalJob):
                logging.info(
                    f"Data is being queried since {job.since} until {job.until},"
                    + f" with schema version number {job.schema_version}"
                )

            objects = self.get_objects(job.id)
            resources = self.get_resources(objects)
        else:
            raise DAPClientError(f"query job ended with status: {job.status.value}")

        return self.download_resources(resources, job.id, output_directory)
