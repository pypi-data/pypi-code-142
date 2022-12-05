import os
import tarfile
import tempfile
import warnings
from typing import Callable, List, Optional

import gitignorefile

from servicefoundry.auto_gen import models
from servicefoundry.lib.clients.service_foundry_client import (
    ServiceFoundryServiceClient,
)
from servicefoundry.logger import logger
from servicefoundry.v2.lib.patched_models import RemoteSource


def _make_tarfile(
    output_filename: str,
    source_dir: str,
    additional_directories: List[str],
    is_path_ignored: Optional[Callable[[str], bool]] = None,
) -> None:
    if not is_path_ignored:
        # if no callback handler present assume that every file needs to be added
        is_path_ignored = lambda *_: False

    with tarfile.open(output_filename, "w:gz") as tar:
        _add_files_in_tar(
            is_path_ignored=is_path_ignored,
            source_dir=source_dir,
            tar=tar,
        )
        for additional_directory in additional_directories:
            _add_files_in_tar(
                is_path_ignored=is_path_ignored,
                source_dir=additional_directory,
                tar=tar,
            )


def _add_files_in_tar(
    is_path_ignored: Callable[[str], bool],
    source_dir: str,
    tar: tarfile.TarFile,
) -> None:
    for root, dirs, files in os.walk(source_dir, topdown=True):
        if is_path_ignored(root):
            logger.debug("Ignoring directory %s", root)

            # NOTE: we can safely ignore going through the sub-dir
            # if root itself is excluded.
            dirs.clear()
            continue
        logger.debug("Adding contents of the directory %s", root)
        for file in files:
            file_path = os.path.join(root, file)
            if not is_path_ignored(file_path):
                arcname = os.path.relpath(file_path, source_dir)
                tar.add(file_path, arcname=arcname)
                logger.debug("Adding %s with arcname %r", file_path, arcname)


def _get_callback_handler_to_ignore_file_path(
    source_dir: str,
) -> Optional[Callable[[str], bool]]:
    ignorefile_path = os.path.join(source_dir, ".tfyignore")
    if os.path.exists(ignorefile_path):
        logger.info(".tfyignore file found in %s", source_dir)
        return gitignorefile.parse(path=ignorefile_path, base_path=source_dir)

    ignorefile_path = os.path.join(source_dir, ".sfyignore")
    if os.path.exists(ignorefile_path):
        logger.info(".sfyignore file found in %s", source_dir)
        warnings.warn(
            "`.sfyignore` is deprecated and will be ignored in future versions. "
            "Please rename the file to `.tfyignore`",
            category=DeprecationWarning,
        )
        return gitignorefile.parse(path=ignorefile_path, base_path=source_dir)

    # check for valid git repo
    try:
        import git

        repo = git.Repo(source_dir, search_parent_directories=True)
        return lambda file_path: repo.ignored([file_path])
    except Exception as ex:
        logger.debug(
            "Could not treat source %r as a git repository due to %r", source_dir, ex
        )

    logger.info(
        "Neither `.tfyignore` file found in %s nor a valid git repository found. "
        "We recommend you to create .tfyignore file and add file patterns to ignore",
        source_dir,
    )
    return None


def local_source_to_remote_source(
    local_source: models.LocalSource,
    workspace_fqn: str,
    component_name: str,
) -> RemoteSource:
    with tempfile.TemporaryDirectory() as local_dir:
        package_local_path = os.path.join(local_dir, "build.tar.gz")
        source_dir = os.path.abspath(local_source.project_root_path)

        if not os.path.exists(source_dir):
            raise ValueError(
                f"project root path {source_dir!r} of component {component_name!r} does not exist"
            )

        logger.info("Uploading contents of %r", source_dir)

        is_path_ignored = _get_callback_handler_to_ignore_file_path(source_dir)

        _make_tarfile(
            output_filename=package_local_path,
            source_dir=source_dir,
            additional_directories=[],
            is_path_ignored=is_path_ignored,
        )
        client = ServiceFoundryServiceClient()
        remote_uri = client.upload_code_package(
            workspace_fqn=workspace_fqn,
            component_name=component_name,
            package_local_path=package_local_path,
        )
        return RemoteSource(remote_uri=remote_uri)
