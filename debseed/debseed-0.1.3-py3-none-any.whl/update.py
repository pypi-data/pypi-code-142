from __future__ import annotations
import argparse
from pathlib import Path
from .utils import command
from .settings import DEFAULT_EDITION, DEFAULT_VARIANT, DEFAULT_ARCH, get_editions, Edition
from .debian import get_last_version, get_iso_url, add_version_argument, add_variant_argument, add_arch_argument
from .download import download
from .generate import generate

def update_add_arguments(parser: argparse.ArgumentParser):
    parser.add_argument('edition', nargs='?', default=DEFAULT_EDITION, help="name of the edition: %s, or path to a preseed.cfg file" % (', '.join(edition + ('*' if edition == DEFAULT_EDITION else '') for edition in get_editions().keys())))
    add_version_argument(parser)
    add_variant_argument(parser)
    add_arch_argument(parser)
    parser.add_argument('--target', help="name or path to the target ISO file")
    parser.add_argument('--publish', '-p', action='store_true', help="publish generated ISO file to external store")
    parser.add_argument('--force', '-f', action='store_true', help="recreate the target ISO file if it already exists")
    parser.add_argument('--keep', '-k', action='store_true', help=f"keep temporary files")

@command(update_add_arguments)
def update(edition: str|Edition = None, version: str = None, variant: str = None, arch: str = None, target: str|Path = None, publish: bool = False, force: bool = False, keep = False):
    """
    Retrieve last available version, download corresponding Debian ISO file and generate custom ISO file from it (if not already done).
    """
    origin = download(version=version, variant=variant, arch=arch)
    generate(origin=origin, edition=edition, target=target, publish=publish, force=force, keep=keep)
