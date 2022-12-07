import sys

DISTRIBUTION_NAME = "datagen-tech"

if sys.version_info < (3, 10):
    from importlib_metadata import version as ver, PackageNotFoundError
else:
    from importlib.metadata import version as ver, PackageNotFoundError


def get_datagen_tech_version():
    try:
        return ver(DISTRIBUTION_NAME)
    except PackageNotFoundError:
        return None


sys.modules[__name__] = get_datagen_tech_version()  # type: ignore
