from __future__ import annotations
import argparse, os, logging
from pathlib import Path
from urllib import request
from .utils import CYAN, RESET, YELLOW, command, verify_gpg_signature, verify_sha256_hash
from .settings import ARCHIVES_ISO_DIR, ORIGIN_ISO_DIR, Edition, get_editions
from .debian import get_last_version, get_iso_url, add_version_argument, add_variant_argument, add_arch_argument
from .external import external

logger = logging.getLogger(__name__)


def check_add_arguments(parser: argparse.ArgumentParser):
    add_version_argument(parser)
    add_variant_argument(parser)
    add_arch_argument(parser)


@command(check_add_arguments)
def check(version: str = None, variant: str = None, arch: str = None) -> Path:
    """
    Retrieve last available Debian version, and check existence of corresponding files.
    """
    version = get_last_version(variant, version)

    # Origin ISO
    origin_iso_url = get_iso_url(variant=variant, arch=arch, version=version)
    origin_iso_path = ORIGIN_ISO_DIR.joinpath(os.path.basename(origin_iso_url))

    if origin_iso_path.exists():
        logger.info("origin ISO found: %s", origin_iso_path)
    else:
        logger.warning("origin ISO not found: %s", origin_iso_path)
        logger.info("origin ISO url: %s", origin_iso_url)

    # Target ISOs
    for edition in get_editions().values():
        _check_edition(edition, origin_iso_path)


def _check_edition(edition: Edition, origin_iso: Path):
    context = edition.get_context(origin_iso.name)
    target_iso = context.target_iso
    
    if target_iso.exists():
        logger.info(f"[edition {edition.name}] target ISO found: {target_iso}")
    elif (archive := ARCHIVES_ISO_DIR.joinpath(target_iso.name)).exists():
        logger.info(f"[edition {edition.name}] target ISO found {YELLOW}in archives{RESET}: {archive}")
    else:
        logger.warning(f"[edition {edition.name}] target ISO not found: {target_iso}")

    if external:
        found = external.exists(target_iso)
        if found:
            logger.info(f"[edition {edition.name}] published ISO found: {found}")
        else:
            logger.warning(f"[edition {edition.name}] published ISO not found in {external}")
