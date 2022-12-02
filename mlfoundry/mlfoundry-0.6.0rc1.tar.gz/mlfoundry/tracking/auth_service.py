import time

from mlflow.utils.rest_utils import MlflowHostCreds, http_request, http_request_safe

from mlfoundry.exceptions import MlFoundryException
from mlfoundry.logger import logger
from mlfoundry.tracking.entities import AuthServerInfo, DeviceCode, Token


class AuthService:
    def __init__(self, auth_server_info: AuthServerInfo):
        self._tenant_name = auth_server_info.tenant_name
        self.host_creds = MlflowHostCreds(host=auth_server_info.auth_server_url)

    def get_token_from_api_key(self, api_key: str) -> Token:
        response = http_request_safe(
            host_creds=self.host_creds,
            endpoint="/api/v1/oauth/api-keys/token",
            method="post",
            json={"apiKey": api_key},
            timeout=3,
            max_retries=0,
        )
        response = response.json()
        return Token.parse_obj(response)

    def refresh_token(self, token: Token) -> Token:
        response = http_request_safe(
            host_creds=self.host_creds,
            endpoint="/api/v1/oauth/token/refresh",
            method="post",
            json={
                "tenantName": token.tenant_name,
                "refreshToken": token.refresh_token,
            },
            timeout=3,
            max_retries=0,
        )
        response = response.json()
        return Token.parse_obj(response)

    def get_device_code(self) -> DeviceCode:
        response = http_request_safe(
            host_creds=self.host_creds,
            endpoint="/api/v1/oauth/device",
            method="post",
            json={"tenantName": self._tenant_name},
            timeout=3,
            max_retries=0,
        )
        response = response.json()
        return DeviceCode.parse_obj(response)

    def get_token_from_device_code(
        self, device_code: str, timeout: float = 60
    ) -> Token:
        start_time = time.monotonic()
        while (time.monotonic() - start_time) <= timeout:
            response = http_request(
                host_creds=self.host_creds,
                endpoint="/api/v1/oauth/device/token",
                method="post",
                json={"tenantName": self._tenant_name, "deviceCode": device_code},
                timeout=3,
                max_retries=0,
            )
            if response.status_code == 202:
                logger.debug("User has not authorized yet. Checking again.")
                time.sleep(1.0)
                continue
            if response.status_code == 201:
                response = response.json()
                return Token.parse_obj(response)
            raise MlFoundryException(
                "Failed to get token using device code. "
                f"status_code {response.status_code},\n {response.text}"
            )
        raise MlFoundryException(f"Did not get authorized within {timeout} seconds.")
