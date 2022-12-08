import os
import netrc
import re
import shutil
from typing import Optional, List, Union

from pydantic import BaseModel, SecretStr, Field, validator

from metaibricks.settings import Settings, Logger
from metaibricks.base import ParallelTaskBase

LOGGER = Logger(name="extraction.session")


class ExtractorBase(ParallelTaskBase):
    """Abstract class for defining an Extractor

    Inherits:
        ParallelTaskBase
    """

    kind: str = Field("Extractor", const=True)


class SessionBase(BaseModel):
    """Abstract class for defining a Session

    Attrs:
        host (Optional[str]):  Host's name
        username (Optional[str]): user's name used to log in. If not provided,
            the one given in .netrc will be used.
        password (Optional[SecretStr]): password associated to the username. If not
            provided, the one given in the .netrc will be used.

    Inherits:
        BaseModel
    """

    host: Optional[str]
    username: Optional[str]
    password: Optional[SecretStr]

    @validator("username", always=True)
    def check_username(cls, v: str, values: dict) -> str:
        """method to validate given user's name or retreiving it if missing."""
        netrc_filename = Settings().netrc_filename
        if v is None and os.path.isfile(netrc_filename):
            creds = netrc.netrc(netrc_filename)
            if values.get("host") in creds.hosts:
                return creds.authenticators(host=values.get("host"))[0]
        return v

    @validator("password", always=True)
    def check_password(cls, v: str, values: dict) -> SecretStr:
        """method to validate and protect given password, or retrieving it if
        missing.
        """
        if isinstance(v, SecretStr):
            return v
        netrc_filename = Settings().netrc_filename
        if v is None and os.path.isfile(netrc_filename):
            creds = netrc.netrc(netrc_filename)
            if values.get("host") in creds.hosts:
                return SecretStr(creds.authenticators(host=values.get("host"))[-1])
        return SecretStr(v)

    def download(self, src_filename: str, tmp_filename: str) -> None:
        """Empty method to download a file from a remote machine.
        It's definition will depend on the transfer protocol.

        Args:
            src_filename (str): Remote source file's name.
            tmp_filename (str): Local destination temporary file's name.
        """
        pass

    def get_subfolders_and_files(self, dirname: str) -> List[str]:
        """Empty method to retrieve the list of subfolders and files of the directory
        "dirname", from a remote machine.
        It's definition will depend on the transfer protocol.

        Args:
            dirname (str): Name of the directory

        Returns:
            List[str]: List of subdirectories and files.
        """
        pass

    def find_pattern(
        self, pattern: str, dirname: Optional[Union[str, List[str]]] = "."
    ) -> List[str]:
        """Method that finds all the directories or files which name matches with
        the given pattern, in the directory "dirname".

        Args:
            pattern (str): Pattern to match.
            dirname (Optional[Union[str, List[str]]]): Directory or list of
                directories where to find matching patterns. Defaults to ".".

        Returns:
            List[str]: List of all the directories or files matching the given pattern.
        """
        if isinstance(dirname, list):
            results = []
            for dname in dirname:
                results.extend(self.find_pattern(pattern, dname))
            return results

        if pattern in ("", "/"):
            # pattern root case
            return ["/"]

        subfolders_files = self.get_subfolders_and_files(dirname)
        subfolders_files = list(dict.fromkeys(subfolders_files))  # remove duplicates
        LOGGER.debug(f"Found following subfolders and files : {subfolders_files}")

        return [
            os.path.join(dirname, basename)
            for basename in subfolders_files
            if re.fullmatch(pattern, basename)
        ]

    def get(self, src_filename: str, dst_filename: str) -> bool:
        """Main method to get a given filename from source and to copy it
        in a destination.

        Args:
            src_filename (str): Remote source file's name.
            dst_filename (str): Local destination file's name.

        Returns:
            bool: Whether the extraction is alright or not.
        """
        log_info = dict(
            host=self.host, src_filename=src_filename, dst_filename=dst_filename
        )
        LOGGER.debug("Trying to get file.", **log_info)

        # checking existing
        if os.path.isfile(dst_filename):
            LOGGER.warning("Destination file already exists: skipping.", **log_info)
            return os.path.isfile(dst_filename)

        # using a tmp file
        dst_abs_filename = os.path.abspath(dst_filename)
        dirname, basename = os.path.split(dst_abs_filename)
        if dirname:
            os.makedirs(dirname, exist_ok=True)
        tmp_filename = os.path.join(dirname, f".{basename}.tmp")

        # extracting file
        try:
            self.download(src_filename, tmp_filename)
            LOGGER.debug("File extracted.", **log_info, tmp_filename=tmp_filename)
        except Exception:
            LOGGER.error("Failed to get file.", **log_info, exc_info=True)
            os.remove(tmp_filename)
            return False

        # renaming file
        if os.path.isfile(tmp_filename):
            shutil.copyfile(tmp_filename, dst_abs_filename)
            LOGGER.debug(
                "Temporary file copied to destination file.",
                tmp_filename=tmp_filename,
                **log_info,
            )
            os.remove(tmp_filename)
            LOGGER.debug(
                "Temporary file removed.", tmp_filename=tmp_filename, **log_info
            )
        else:
            LOGGER.error(
                "Failed to create temporary file.",
                tmp_filename=tmp_filename,
                **log_info,
            )
            return False

        if not os.path.isfile(dst_filename):
            LOGGER.error("File extraction failed.", **log_info)

        LOGGER.info("File correctly extracted.", **log_info)
        return True
