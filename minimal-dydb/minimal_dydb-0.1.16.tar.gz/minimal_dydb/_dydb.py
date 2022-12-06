import asyncio
from urllib.parse import urlparse

import httpx

from minimal_dydb._aws_auth import AWSRequestsAuth
from minimal_dydb._credential_managers import CredentialManagerBase

# api https://docs.aws.amazon.com/amazondynamodb/latest/APIReference


_DESCRIBE_TABLE_TARGET = {"X-Amz-Target": f"DynamoDB_20120810.DescribeTable"}
_GET_TARGET = {"X-Amz-Target": f"DynamoDB_20120810.GetItem"}
_PUT_TARGET = {"X-Amz-Target": f"DynamoDB_20120810.PutItem"}
_QUERY_TARGET = {"X-Amz-Target": f"DynamoDB_20120810.Query"}
_SCAN_TARGET = {"X-Amz-Target": f"DynamoDB_20120810.Scan"}
_DELETE_TARGET = {"X-Amz-Target": f"DynamoDB_20120810.DeleteItem"}
_BATCH_GET_TARGET = {"X-Amz-Target": f"DynamoDB_20120810.BatchGetItem"}
_BATCH_WRITE_TARGET = {"X-Amz-Target": f"DynamoDB_20120810.BatchWriteItem"}
_CREATE_TABLE_TARGET = {"X-Amz-Target": f"DynamoDB_20120810.CreateTable"}

_AWS_SERVICE = "dynamodb"


# def _get_target_dict(target: str):
#     return {"X-Amz-Target": f"DynamoDB_20120810.{target}"}
#
# def _gen_sync_method(cls, func_name: str, target: str):
#     target_dict = _get_target_dict(target)
#
#     def func(self, **kwargs):
#         resp = self._s.post(
#             self._url,
#             data=kwargs,
#             headers=target_dict,
#             auth=self._get_aws_auth(),
#         )
#         return resp
#
#     setattr(cls, func_name, classmethod(func))
#
#
# def _gen_async_method(cls, func_name: str, target: str):
#     target_dict = _get_target_dict(target)
#
#     async def func(self, **kwargs):
#         resp = self._s.post(
#             self._url,
#             data=kwargs,
#             headers=target_dict,
#             auth=self._get_aws_auth(),
#         )
#         return resp
#
#     setattr(cls, func_name, classmethod(func))


class SyncDynamoDB:
    def __init__(
        self,
        *,
        credential_manager: CredentialManagerBase,
        region: str,
        endpoint: str,
    ):
        self.__credential_manager = credential_manager

        self._url = endpoint
        self._netlock = urlparse(self._url).netloc

        self._s = httpx.Client(headers={"Content-Type": "application/json"})
        self._region = region

    def __del__(self):
        try:
            self._s.close()
        except:
            pass

    def _get_aws_auth(self):
        creds = self.__credential_manager.get_credentials()
        return AWSRequestsAuth(
            aws_access_key=creds.aws_access_key,
            aws_secret_access_key=creds.aws_secret_key,
            aws_host=self._netlock,
            aws_region=self._region,
            aws_service=_AWS_SERVICE,
            aws_token=creds.aws_session_token,
        )

    def describe_table(self, json_bytes: bytes):
        resp = self._s.post(
            self._url,
            content=json_bytes,
            headers=_DESCRIBE_TABLE_TARGET,
            auth=self._get_aws_auth(),
        )
        return resp

    def get_item(self, json_bytes: bytes):
        resp = self._s.post(
            self._url,
            content=json_bytes,
            headers=_GET_TARGET,
            auth=self._get_aws_auth(),
        )
        return resp

    def put_item(self, json_bytes: bytes):
        resp = self._s.post(
            self._url,
            content=json_bytes,
            headers=_PUT_TARGET,
            auth=self._get_aws_auth(),
        )
        return resp

    def query(self, json_bytes: bytes):
        resp = self._s.post(
            self._url,
            content=json_bytes,
            headers=_QUERY_TARGET,
            auth=self._get_aws_auth(),
        )
        return resp

    def scan(self, json_bytes: bytes):
        resp = self._s.post(
            self._url,
            content=json_bytes,
            headers=_SCAN_TARGET,
            auth=self._get_aws_auth(),
        )
        return resp

    def batch_get(self, json_bytes: bytes):
        resp = self._s.post(
            self._url,
            content=json_bytes,
            headers=_BATCH_GET_TARGET,
            auth=self._get_aws_auth(),
        )
        return resp

    def batch_write(self, json_bytes: bytes):
        resp = self._s.post(
            self._url,
            content=json_bytes,
            headers=_BATCH_WRITE_TARGET,
            auth=self._get_aws_auth(),
        )
        return resp

    def delete(self, json_bytes: bytes):
        resp = self._s.post(
            self._url,
            content=json_bytes,
            headers=_DELETE_TARGET,
            auth=self._get_aws_auth(),
        )
        return resp

    def create_table(self, json_bytes: bytes):
        resp = self._s.post(
            self._url,
            content=json_bytes,
            headers=_CREATE_TABLE_TARGET,
            auth=self._get_aws_auth(),
        )
        return resp


class AsyncDynamoDB:
    def __init__(
        self,
        *,
        credential_manager: CredentialManagerBase,
        region: str,
        endpoint: str,
    ):
        self.__credential_manager = credential_manager

        self._url = endpoint
        self._netlock = urlparse(self._url).netloc

        self._s = httpx.AsyncClient(headers={"Content-Type": "application/json"})
        self._region = region

    def __del__(self):
        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self._s.aclose)
        except:
            pass

    def _get_aws_auth(self):
        creds = self.__credential_manager.get_credentials()
        return AWSRequestsAuth(
            aws_access_key=creds.aws_access_key,
            aws_secret_access_key=creds.aws_secret_key,
            aws_host=self._netlock,
            aws_region=self._region,
            aws_service=_AWS_SERVICE,
            aws_token=creds.aws_session_token,
        )

    async def describe_table(self, json_bytes: bytes):
        resp = await self._s.post(
            self._url,
            content=json_bytes,
            headers=_DESCRIBE_TABLE_TARGET,
            auth=self._get_aws_auth(),
        )
        return resp

    async def get_item(self, json_bytes: bytes):
        resp = await self._s.post(
            self._url,
            content=json_bytes,
            headers=_GET_TARGET,
            auth=self._get_aws_auth(),
        )
        return resp

    async def put_item(self, json_bytes: bytes):
        resp = await self._s.post(
            self._url,
            content=json_bytes,
            headers=_PUT_TARGET,
            auth=self._get_aws_auth(),
        )
        return resp

    async def query(self, json_bytes: bytes):
        resp = await self._s.post(
            self._url,
            content=json_bytes,
            headers=_QUERY_TARGET,
            auth=self._get_aws_auth(),
        )
        return resp

    async def scan(self, json_bytes: bytes):
        resp = await self._s.post(
            self._url,
            content=json_bytes,
            headers=_SCAN_TARGET,
            auth=self._get_aws_auth(),
        )
        return resp

    async def batch_get(self, json_bytes: bytes):
        resp = await self._s.post(
            self._url,
            content=json_bytes,
            headers=_BATCH_GET_TARGET,
            auth=self._get_aws_auth(),
        )
        return resp

    async def batch_write(self, json_bytes: bytes):
        resp = await self._s.post(
            self._url,
            content=json_bytes,
            headers=_BATCH_WRITE_TARGET,
            auth=self._get_aws_auth(),
        )
        return resp

    async def delete(self, json_bytes: bytes):
        resp = await self._s.post(
            self._url,
            content=json_bytes,
            headers=_DELETE_TARGET,
            auth=self._get_aws_auth(),
        )
        return resp

    async def create_table(self, json_bytes: bytes):
        resp = await self._s.post(
            self._url,
            content=json_bytes,
            headers=_CREATE_TABLE_TARGET,
            auth=self._get_aws_auth(),
        )
        return resp
