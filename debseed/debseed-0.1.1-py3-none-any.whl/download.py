from __future__ import annotations
import argparse, os, logging
from pathlib import Path
from urllib import request
from .utils import CYAN, RESET, command, verify_gpg_signature, verify_sha256_hash
from .settings import DEBIAN_CD_SIGNING_KEY, DEFAULT_VARIANT, DEFAULT_ARCH, ORIGIN_ISO_DIR
from .debian import get_last_version, get_iso_url, add_version_argument, add_variant_argument, add_arch_argument

logger = logging.getLogger(__name__)


def download_add_arguments(parser: argparse.ArgumentParser):
    add_version_argument(parser)
    add_variant_argument(parser)
    add_arch_argument(parser)
    parser.add_argument('--verify', action='store_true', help="force verification of checksum")


@command(download_add_arguments)
def download(version: str = None, variant: str = None, arch: str = None, verify: bool = False) -> Path:
    """
    Download origin Debian ISO files.

    Returns path to ISO file.
    """
    version = get_last_version(variant, version)

    iso_url = get_iso_url(variant=variant, arch=arch, version=version)

    # Download ISO if needed
    ORIGIN_ISO_DIR.mkdir(parents=True, exist_ok=True)
    iso_path = ORIGIN_ISO_DIR.joinpath(os.path.basename(iso_url))
    if iso_path.exists():
        logger.info("file already exist: %s", iso_path)
    else:
        logger.info("download %s", iso_url)
        request.urlretrieve(iso_url, iso_path)
        logger.info("file downloaded: %s", iso_path)
        verify = True

    if verify:
        dir_url = os.path.dirname(iso_url)
        sums_path = ORIGIN_ISO_DIR.joinpath('sha256sums', variant + '_' + '_'.join(dir_url.split('/')[-3:]) + '.SHA256SUMS')
        sums_path.parent.mkdir(parents=True, exist_ok=True)
        sign_path = sums_path.parent.joinpath(sums_path.name + '.sign')

        # Download SHA256SUMS if needed
        sums_url = f"{dir_url}/SHA256SUMS"
        if not sums_path.exists():
            logger.info("download %s", sums_url)
            request.urlretrieve(sums_url, sums_path)

        # Download SHA256SUMS.sign if needed
        sign_url = f"{dir_url}/SHA256SUMS.sign"
        if not sign_path.exists():
            logger.info("download %s", sign_url)
            request.urlretrieve(sign_url, sign_path)
        
        # Verify
        verify_gpg_signature(sign_path, DEBIAN_CD_SIGNING_KEY)
        verify_sha256_hash(iso_path, sums_path)

    return iso_path
