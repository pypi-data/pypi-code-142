from sys import version_info

if version_info >= (3, 8):
    from importlib import metadata as metadata  # type: ignore
else:
    import importlib_metadata as metadata  # type: ignore

__version__ = metadata.version(__package__)
