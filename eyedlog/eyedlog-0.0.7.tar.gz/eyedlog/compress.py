# coding: utf-8

import argparse
import zipfile
from pathlib import Path


ZipSuffixDict = {
    'zip': zipfile.ZIP_DEFLATED,
    'bz2': zipfile.ZIP_BZIP2,
    'lzma': zipfile.ZIP_LZMA,
}


def lookup_zip_format(fmt):
    if fmt in ZipSuffixDict:
        return ZipSuffixDict[fmt]
    return zipfile.ZIP_STORED


def act(source, target, compression='bz2'):
    comp = lookup_zip_format(compression)
    archive = Path(source).name
    with zipfile.ZipFile(target, 'w', compression=comp) as zf:
        zf.write(source, arcname=archive)
    if Path(source).exists():
        Path(source).unlink()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='EyedLog',
        description='For compressing logs',
        epilog='Help'
    )
    parser.add_argument('-s', '--source', required=True, help='Source file to be zipped')
    parser.add_argument('-t', '--target', required=True, help='Target file')
    parser.add_argument('-c', '--compression', default='bz2', choices=['zip', 'bz2', 'lzma'],
                        help='Compression method, default "bz2"')
    args, unknown = parser.parse_known_args()
    if args:
        act(args.source, args.target, args.compression)
