import configparser
import pathlib
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass
from os import environ
from threading import Thread
from typing import Optional

import httpx
import pydantic

from minimal_dydb._config import logger


@dataclass
class AWSCredentials:
    aws_access_key: str
    aws_secret_key: str
    aws_session_token: Optional[str] = None


class CredentialManagerBase(ABC):
    @abstractmethod
    def get_credentials(self) -> AWSCredentials:  # pragma: no cover
        return AWSCredentials(aws_access_key="foo", aws_secret_key="bazz")


class _CredentialManagerEnv(pydantic.BaseModel):
    access_key_var_name: pydantic.constr(min_length=1)
    secret_key_var_name: pydantic.constr(min_length=1)
    session_token_var_name: Optional[pydantic.constr(min_length=1)] = None
    refresh_after: Optional[pydantic.conint(gt=0) | pydantic.confloat(gt=0)] = None


class CredentialManagerEnv(CredentialManagerBase):
    def __init__(
        self,
        *,
        access_key_var_name: str = "AWS_ACCESS_KEY_ID",
        secret_key_var_name: str = "AWS_SECRET_ACCESS_KEY",
        session_token_var_name: Optional[str] = "AWS_SESSION_TOKEN",
        refresh_after: Optional[int | float] = None,
    ):
        _CredentialManagerEnv(
            access_key_var_name=access_key_var_name,
            secret_key_var_name=secret_key_var_name,
            session_token_var_name=session_token_var_name,
            refresh_after=refresh_after,
        )

        self.__access_key_var_name = access_key_var_name
        self.__secret_key_var_name = secret_key_var_name
        self.__session_token_var_name = session_token_var_name
        self.__refresh_after = refresh_after

        self._set_credentials()
        if refresh_after:
            thread = Thread(target=self._refresh_credentials)
            thread.daemon = True
            thread.start()

    def _refresh_credentials(self):
        while True:
            time.sleep(self.__refresh_after)
            self._set_credentials()

    def _set_credentials(self):
        self.__credentials = AWSCredentials(
            aws_access_key=environ[self.__access_key_var_name],
            aws_secret_key=environ[self.__secret_key_var_name],
            aws_session_token=environ.get(self.__session_token_var_name, None),
        )

    def get_credentials(self) -> AWSCredentials:
        return self.__credentials


class _CredentialManagerArgs(pydantic.BaseModel):
    aws_access_key: pydantic.constr(min_length=1)
    aws_secret_key: pydantic.constr(min_length=1)
    aws_session_token: Optional[pydantic.constr(min_length=1)] = None


class CredentialManagerArgs(CredentialManagerBase):
    def __init__(
        self,
        *,
        aws_access_key: str,
        aws_secret_key: str,
        aws_session_token: Optional[str] = None,
    ):
        _CredentialManagerArgs(
            aws_access_key=aws_access_key,
            aws_secret_key=aws_secret_key,
            aws_session_token=aws_session_token,
        )

        self.__credentials = AWSCredentials(
            aws_access_key=aws_access_key,
            aws_secret_key=aws_secret_key,
            aws_session_token=aws_session_token,
        )

    def get_credentials(self) -> AWSCredentials:
        return self.__credentials


class _CredentialManagerFileArgs(pydantic.BaseModel):
    file_path: pydantic.FilePath
    profile_name: pydantic.constr(min_length=1)
    refresh_after: Optional[pydantic.conint(gt=0) | pydantic.confloat(gt=0)] = None


class CredentialManagerFile(CredentialManagerBase):
    def __init__(
        self,
        *,
        file_path: str | pathlib.Path = "~/.aws/credentials",
        profile_name: str = "default",
        refresh_after: Optional[int | float] = None,
    ):
        if type(file_path) == str:
            file_path = pathlib.Path(file_path)

        full_path = file_path.expanduser().resolve()
        args = _CredentialManagerFileArgs(
            file_path=full_path, profile_name=profile_name, refresh_after=refresh_after
        )

        self.__file_path = args.file_path
        self.__profile_name = args.profile_name
        self.__refresh_after = args.refresh_after

        self._set_credentials()
        if refresh_after:
            thread = Thread(target=self._refresh_credentials)
            thread.daemon = True
            thread.start()

    def _refresh_credentials(self):
        while True:
            time.sleep(self.__refresh_after)
            self._set_credentials()

    def _set_credentials(self):
        config_parser = configparser.ConfigParser()
        with open(self.__file_path, "r") as f:
            config_parser.read_file(f)

        self.__credentials = AWSCredentials(
            aws_access_key=config_parser.get(self.__profile_name, "aws_access_key_id"),
            aws_secret_key=config_parser.get(
                self.__profile_name, "aws_secret_access_key"
            ),
            aws_session_token=config_parser.get(
                self.__profile_name, "aws_session_token", fallback=None
            ),
        )

    def get_credentials(self) -> AWSCredentials:
        return self.__credentials


class _CredentialManagerMetadataService(pydantic.BaseModel):
    url: pydantic.HttpUrl
    refresh_after: Optional[pydantic.conint(gt=0) | pydantic.confloat(gt=0)] = None


class CredentialManagerMetadataService(CredentialManagerBase):
    def __init__(
        self,
        url: str = "http://169.254.169.254",
        refresh_after: Optional[int | float] = None,
    ):

        _CredentialManagerMetadataService(url=url, refresh_after=refresh_after)
        self._url = url

        self.__refresh_after = refresh_after

        self._set_credentials()

        if refresh_after:
            thread = Thread(target=self._refresh_credentials)
            thread.daemon = True
            thread.start()

    def _refresh_credentials(self):
        while True:
            time.sleep(self.__refresh_after)
            self._set_credentials()

    def _set_credentials(self):
        token_resp = httpx.put(
            f"{self._url}/latest/api/token",
            headers={"X-aws-ec2-metadata-token-ttl-seconds": "10"},
        )
        if token_resp.status_code == 200:
            headers = {"X-aws-ec2-metadata-token": token_resp.text}
        else:
            headers = {}
        resp = httpx.get(
            f"{self._url}/latest/meta-data/iam/security-credentials/", headers=headers
        )
        role = resp.text
        resp = httpx.get(
            f"{self._url}/latest/meta-data/iam/security-credentials/{role}",
            headers=headers,
        )
        resp_dict = resp.json()
        self.__credentials = AWSCredentials(
            aws_access_key=resp_dict["AccessKeyId"],
            aws_secret_key=resp_dict["SecretAccessKey"],
            aws_session_token=resp_dict.get("Token", None),
        )

    def get_credentials(self) -> AWSCredentials:
        return self.__credentials


def auto_credential_manager():
    logger.info("Looking for AWS credentials")
    try:
        credmanager = CredentialManagerEnv()
        credmanager.get_credentials()
        logger.info("Found aws credentials in environment")
        return credmanager
    except Exception as e:
        pass

    try:
        credentials_file = "~/.aws/credentials"
        credmanager = CredentialManagerFile(
            file_path=credentials_file, refresh_after=30
        )
        credmanager.get_credentials()
        logger.info(f"Found aws credentials in {credentials_file} file")
        return credmanager
    except Exception as e:
        pass

    try:
        config_file = "~/.aws/config"
        credmanager = CredentialManagerFile(file_path=config_file, refresh_after=30)
        credmanager.get_credentials()
        logger.info(f"Found aws credentials in {config_file} file")

        return credmanager
    except Exception as e:
        pass

    try:
        credmanager = CredentialManagerMetadataService(refresh_after=30)
        credmanager.get_credentials()
        logger.info(f"Found aws credentials in metadata service")
        return credmanager
    except Exception as e:
        pass

    raise Exception(
        "Unable to find valid aws credentials to use, please pass in a manager"
    )
