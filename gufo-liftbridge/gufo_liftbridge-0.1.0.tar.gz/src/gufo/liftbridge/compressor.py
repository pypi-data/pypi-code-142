# ----------------------------------------------------------------------
# Gufo Liftbridge: Compression utilities
# ----------------------------------------------------------------------
# Copyright (C) 2022, Gufo Labs
# See LICENSE.md for details
# ----------------------------------------------------------------------

# Python modules
from typing import cast, Callable, Dict, Tuple

TCompressor = Callable[[bytes], bytes]
TDecompressor = Callable[[bytes], bytes]


_COMPRESSORS: Dict[str, TCompressor] = {}
_DECOMPRESSORS: Dict[str, TDecompressor] = {}


def _get_zlib() -> Tuple[TCompressor, TDecompressor]:
    from zlib import compress as z_compress, decompress as z_decompress

    return cast(TCompressor, z_compress), cast(TDecompressor, z_decompress)


def _get_lzma() -> Tuple[TCompressor, TDecompressor]:
    from lzma import compress as lzma_compress, decompress as lzma_decompress

    return cast(TCompressor, lzma_compress), cast(
        TDecompressor, lzma_decompress
    )


_handlers = {"zlib": _get_zlib, "lzma": _get_lzma}


def _get_handlers(method: str) -> Tuple[TCompressor, TDecompressor]:
    try:
        return _handlers[method]()
    except KeyError:
        raise ValueError(f"Invalid compression method: {method}")


def compress(value: bytes, method: str) -> bytes:
    """
    Compress `value` with given `method`.

    Args:
        value: Uncompressed value.
        method: Compression method, one of: `zlib`, `lzma`.

    Returns:
        Compressed value.

    Raises:
        ValueError: On invalid `method`.
    """
    comp = _COMPRESSORS.get(method)
    if comp is None:
        comp, _ = _get_handlers(method)
        _COMPRESSORS[method] = comp
    return comp(value)


def decompress(value: bytes, method: str) -> bytes:
    """
    Decompress `value` with given `method`.

    Args:
        value: Compressed value.
        method: Compression method, one of: `zlib`, `lzma`.

    Returns:
        Decompressed value.

    Raises:
        ValueError: On invalid `method`.
    """
    decomp = _DECOMPRESSORS.get(method)
    if decomp is None:
        _, decomp = _get_handlers(method)
        _DECOMPRESSORS[method] = decomp
    return decomp(value)
