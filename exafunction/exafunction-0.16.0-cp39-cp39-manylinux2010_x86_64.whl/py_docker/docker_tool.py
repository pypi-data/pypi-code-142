# Copyright Exafunction, Inc.

"""Entry point for the Exafunction docker tool."""

import logging
import os
import os.path
import shutil
import sys
import tempfile
import textwrap

from exa.py_docker import docker_templates
from exa.py_docker import docker_wrappers


def _apply_tar(args):
    dockerfile = (
        docker_templates.Dockerfile.from_image(args.image)
        .apply_layer_tar(args.archive)
        .contents
    )
    docker_wrappers.build_image(dockerfile, tag=args.tag)


def _apply_requirements(args):
    dockerfile = (
        docker_templates.Dockerfile.from_image(args.image)
        .apply_pip_requirements_txt(args.requirements_txt)
        .contents
    )
    docker_wrappers.build_image(dockerfile, tag=args.tag)


_METADATA_PATH = "/tmp/exafunction/module_repository/metadata"
_CACHE_PATH = "/tmp/exafunction/module_repository/cache"


def _save_snapshot(args):
    """Copy the tmp directory over to a user-specified location"""
    # We have to copy from /tmp to a directory Docker can access with ADD.
    with tempfile.TemporaryDirectory(dir=os.getcwd()) as temp_dir:
        relative_path = temp_dir[len(os.getcwd()) :]
        shutil.copytree(
            _METADATA_PATH,
            temp_dir + "/metadata",
            dirs_exist_ok=True,
        )
        shutil.copytree(
            _CACHE_PATH,
            temp_dir + "/cache",
            dirs_exist_ok=True,
        )
        dockerfile = textwrap.dedent(
            f"""\
            FROM {args.image}

            ADD {relative_path}/metadata/ {_METADATA_PATH}/

            ADD {relative_path}/cache/ {_CACHE_PATH}/
            """
        )
        docker_wrappers.build_image(dockerfile, tag=args.tag)


def setup_parser(subparser):
    """Sets up the argument subparser"""

    subparser.add_argument(
        "--image",
        type=str,
        required=True,
        help="What you would put after FROM in the Dockerfile",
    )

    cmd_parsers = subparser.add_subparsers()
    apply_tar_parser = cmd_parsers.add_parser(
        "apply_tar", help="Add Exafunction layer archive to image"
    )
    apply_tar_parser.add_argument("--tag", type=str)
    apply_tar_parser.add_argument("archive", help="Filename or URL for the archive")
    apply_tar_parser.set_defaults(tool_cmd=_apply_tar)

    apply_requirements_parser = cmd_parsers.add_parser(
        "apply_requirements", help="Add pip requirements to image"
    )
    apply_requirements_parser.add_argument("--tag", type=str)
    apply_requirements_parser.add_argument(
        "requirements_txt", help="Filename or URL for the requirements.txt"
    )
    apply_requirements_parser.set_defaults(tool_cmd=_apply_requirements)
    snapshot_parser = cmd_parsers.add_parser(
        "snapshot_local_e2e", help="Save a snapshot of the module repository"
    )
    snapshot_parser.add_argument("--tag", type=str)
    snapshot_parser.set_defaults(tool_cmd=_save_snapshot)


def main(args):
    """The main function for this tool"""
    if not hasattr(args, "tool_cmd"):
        args.tool_parser.print_help()
        logging.error("error: missing tool command")
        sys.exit(-1)
    args.tool_cmd(args)
