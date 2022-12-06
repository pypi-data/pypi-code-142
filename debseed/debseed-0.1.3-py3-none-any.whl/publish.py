from __future__ import annotations
import os, sys, shutil, subprocess, argparse, shutil, shlex, logging
from pathlib import Path
from jinja2 import Template
from .utils import command, without_j2
from .settings import ORIGIN_ISO_DIR, TARGET_ISO_DIR, ARCHIVES_ISO_DIR, Context, Edition, get_edition, get_editions, DEFAULT_EDITION
from .external import external

logger = logging.getLogger(__name__)

def publish_add_arguments(parser: argparse.ArgumentParser):
    parser.add_argument('local', help="name or path to the local ISO file")
    parser.add_argument('--force', '-f', action='store_true', help="recreate the published ISO file if it already exists")


@command(publish_add_arguments)
def publish(local: str|Path, force: bool = False):
    """
    Publish ISO file to external store.
    """
    if not external:
        logger.error(f"cannot publish: no external store configured")
        return

    if isinstance(local, str):
        if os.path.exists(local):
            local = Path(local)
        else:
            local = TARGET_ISO_DIR.joinpath(local)

    if not force:
        found = external.exists(local)
        if found:
            logger.warning(f"file already published on {found}")
            return

    logger.info(f"publish {local}")
    external.publish(local)
