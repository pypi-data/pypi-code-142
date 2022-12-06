import pkg_resources

PROGRAM_NAME = "delink"

try:
    __version__ = pkg_resources.get_distribution(PROGRAM_NAME).version
except pkg_resources.DistributionNotFound:
    __version__ = "unknown"

if __name__ == "__main__":
    print(__version__)
