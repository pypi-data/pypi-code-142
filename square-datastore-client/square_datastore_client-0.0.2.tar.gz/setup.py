from setuptools import setup, find_packages

__version__ = "0.0.2"

setup(
    name="square_datastore_client",
    version=__version__,
    license="MIT",
    description="",
    url="https://github.com/UKP-SQuARE/square-datastore-client",
    download_url=f"https://github.com/UKP-SQuARE/square-datastore-client/archive/refs/tags/v{__version__}.tar.gz",
    author="UKP",
    author_email="baumgaertner@ukp.informatik.tu-darmstadt.de",
    packages=find_packages(
        exclude=(
            "Makefile",
            ".gitignore",
            "requirements.dev.txt",
            ".pre-commit-config.yaml",
        )
    ),
    install_requires=["requests>=2.28.1", "square-auth>=0.0.14"],
)
