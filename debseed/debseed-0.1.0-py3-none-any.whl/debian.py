from __future__ import annotations
from pathlib import Path
import re, logging, os, argparse
from urllib import request
from distutils.version import StrictVersion
from debseed.utils import CYAN, RESET
from .settings import DEFAULT_VARIANT, DEFAULT_ARCH

logger = logging.getLogger(__name__)

VERSION_NAMES = {
    14: 'forky',
    13: 'trixie',
    12: 'bookworm',
    11: 'bullseye',
    10: 'buster',
    9: 'stretch',
    8: 'jessie',
    7: 'wheezy',
    6: 'squeeze',
    5: 'lenny',
    4: 'etch',
}

NAME_VERSIONS = {
    name: major_version for major_version, name in VERSION_NAMES.items()
}

AVAILABLE_VARIANTS = ["firmware", "debian"]
AVAILABLE_ARCHS = ["amd64-i386", "amd64", "i386", "arm64", "armel", "armhf", "mips", "mips64el", "mipsel", "ppc64el", "s390x"]

def add_version_argument(parser: argparse.ArgumentParser):
    parser.add_argument('version', nargs='?', help=f"version of Debian: number (e.g. '11', '11.5') or name (e.g. 'bullseye')")

def add_variant_argument(parser: argparse.ArgumentParser):
    parser.add_argument('--variant', default=DEFAULT_VARIANT, help="variant of the CD distribution: " + ', '.join(val + ('*' if val == DEFAULT_VARIANT else '') for val in AVAILABLE_VARIANTS))

def add_arch_argument(parser: argparse.ArgumentParser):
    parser.add_argument('--arch', default=DEFAULT_ARCH, help="computer architecture: " + ', '.join(val + ('*' if val == DEFAULT_ARCH else '') for val in AVAILABLE_ARCHS))


FULL_VERSION_PATTERN = re.compile(r'^(\d+)\.(\d+)\.(\d+)$')

_versions: dict[str,dict[str, bool]] = {}

def get_base_url(variant: str, in_archive: bool = None):
    base = "https://cdimage.debian.org/cdimage/"
    if variant == "firmware":
        base += "unofficial/non-free/cd-including-firmware/"

    if in_archive:
        base += "archive/"
    else:
        if variant != "firmware":
            base += "release/"
    
    return base


def get_versions(variant: str) -> dict[str, bool]:
    nonarchive_url = get_base_url(variant)

    if not nonarchive_url in _versions:
        versions = {}

        # Read release URL
        logger.info("analyze %s", nonarchive_url)
        response = request.urlopen(nonarchive_url)
        found = re.findall(r"<a href=\"(\d+\.\d+\.\d+)[^\"]*\">", response.read().decode(response.headers.get_content_charset()))
        found.sort(key=StrictVersion, reverse=True)
        if len(found) == 0:
            raise ValueError(f"no version found at {nonarchive_url}")
        for version in found:
            if not version in versions:
                versions[version] = False # not in archive

        # Read archive URL
        archive_url = get_base_url(variant, in_archive=True)
        logger.info("analyze %s", archive_url)
        response = request.urlopen(archive_url)
        found = re.findall(r"<a href=\"(\d+\.\d+\.\d+)[^\"]*\">", response.read().decode(response.headers.get_content_charset()))
        found.sort(key=StrictVersion, reverse=True)
        if len(found) == 0:
            raise ValueError(f"no version found at {archive_url}")
        for version in found:
            if not version in versions:
                versions[version] = True # in archive

        _versions[nonarchive_url] = versions

    return _versions[nonarchive_url]


def get_iso_url(variant: str, arch: str, version: str):
    versions = get_versions(variant)
    if not version in versions:
        raise ValueError(f"version not found: {version}")

    in_archive = versions[version]

    base = get_base_url(variant=variant, in_archive=in_archive)
    
    if arch == 'amd64-i386':
        arch_path = 'multi-arch'
    else:
        arch_path = arch

    if variant == 'firmware':
        version_suffix = '+nonfree'
    else:
        version_suffix = ''
        
    return base + f"{version}{version_suffix}/{arch_path}/iso-cd/{variant}-{version}-{arch}-netinst.iso"


def parse_iso_name(iso: Path|str) -> tuple[str,str,str,str]:
    """
    Returns: edition, version, variant, arch
    """
    if isinstance(iso, Path):
        name = iso.name
    else:
        name = os.path.basename(iso)

    m = re.match(r"^(?P<prefix>.+)\-(?P<version>\d+\.\d+\.\d+)\-(?P<arch>.+)\-netinst\.iso$", name)
    if not m:
        try:
            version = extract_debian_full_version(name)
        except:
            version = None
        return None, version, None, None

    prefix = m.group('prefix')
    version = m.group('version')
    arch = m.group('arch')

    edition = None
    variant = None
    for v in AVAILABLE_VARIANTS:
        if prefix.endswith(f'-{v}'):
            edition = prefix[:-len(f'-{v}')]
            variant = v
            break
    
    return edition, version, variant, arch


def extract_debian_full_version(iso_name: str) -> str:
    if m := re.match(r'.*\-(\d+\.\d+\.\d+)\-.*', iso_name):
        return m.group(1)
    else:
        raise ValueError(f"debian version not found in {iso_name}")


def get_debian_major_version(version: str) -> int:
    if isinstance(version, int):
        return version
        
    if re.match(r'^\d+$', version):
        return int(version)

    if (l := version.lower()) in NAME_VERSIONS:
        return NAME_VERSIONS[l]

    m = FULL_VERSION_PATTERN.match(version)

    if not m:
        version = extract_debian_full_version(version)
        m = FULL_VERSION_PATTERN.match(version)

    return int(m.group(1))


def get_debian_version_name(version: str) -> str:
    major_version = get_debian_major_version(version)
    if major_version in VERSION_NAMES:
        return VERSION_NAMES[major_version]
    else:
        raise ValueError(f"name unknown for debian version {version}")


def get_last_version(variant: str, spec: str = None) -> str:
    if isinstance(spec, str) and FULL_VERSION_PATTERN.match(spec):
        return spec

    versions = get_versions(variant).keys()

    if not spec:
        for version in versions:
            logger.info(f"{CYAN}latest available Debian version: {version}{RESET}")
            return version

    else:
        if re.match(r"^\d+\.\d+$", spec):
            start = spec
        else:
            major_version = get_debian_major_version(spec)
            start = f"{major_version}."

        for version in versions:
            if version.startswith(start):
                logger.info(f"{CYAN}latest available Debian version for {spec}: {version}{RESET}")
                return version

    return ValueError(f"no version found for {spec}")
