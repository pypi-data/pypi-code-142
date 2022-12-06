# Copyright Exafunction, Inc.

"""Convenience utilities for Docker image construction."""

from dataclasses import dataclass
import json
import subprocess
from typing import List, Optional, Tuple, Union

import docker

from exa.py_docker import docker_templates
from exa.py_docker import docker_wrappers


@dataclass
class Image:
    """Metadata for a Docker image."""

    repository: str
    tag: Optional[str] = None
    digest: Optional[str] = None
    builtin_framework: Optional[str] = None
    builtin_framework_version: Optional[str] = None
    python_version: Optional[Tuple[int, int]] = None
    cuda_version: Optional[Tuple[int, int]] = None
    has_conda: bool = False
    dockerfile: Optional[str] = None

    def from_arg(self):
        """Return the FROM argument for a Dockerfile."""
        if self.digest is not None:
            return f"{self.repository}@{self.digest}"
        return f"{self.repository}:{self.tag}"


@dataclass
class RunnerLayer:
    """Metadata for a runner layer."""

    url: str
    cuda_version: Tuple[int, int]
    python_version: Tuple[int, int]

    def compatible_with(self, image: Image):
        """Return whether this layer is compatible with the given image."""
        if image.cuda_version is None:
            return False
        # Only check major version.
        if image.cuda_version[0] != self.cuda_version[0]:
            return False
        if self.python_version != image.python_version:
            return False
        return True


_KNOWN_RUNNER_LAYERS = [
    RunnerLayer(
        url=(
            "https://storage.googleapis.com/exafunction-dist/"
            "exafunction_runner_layer-9b4nmxgvsruiiBnAfp-6bf8ac6d6752.tar.gz"
        ),
        cuda_version=(11, 0),
        python_version=(3, 7),
    ),
]


def torch_base_image() -> Image:
    """Returns a recent PyTorch image."""
    return Image(
        repository="pytorch/pytorch",
        tag="1.12.1-cuda11.3-cudnn8-runtime",
        digest=(
            "sha256:0bc0971dc8ae319af610d493aced87df46255c9508a8b9e9bc365f11a56e7b75"
        ),
        builtin_framework="pytorch",
        builtin_framework_version="1.12.1",
        python_version=(3, 7),
        cuda_version=(11, 3),
        has_conda=True,
    )


_KNOWN_BASE_IMAGES = {
    "pytorch": torch_base_image(),
}


def create_runner_image(
    base_image: Union[str, Image],
    repository: str,
    tag: str,
    *,
    apt_packages: Optional[List[str]] = None,
    yum_packages: Optional[List[str]] = None,
    conda_packages: Optional[List[str]] = None,
    pip_requirements: Optional[List[str]] = None,
) -> Image:
    """
    Creates a Docker image with the Exafunction runner binary installed.

    :param base_image: The base image to use.
    :param repository: The repository to push the image to, including the registry.
        For example, `gcr.io/example/repository`.
    :param tag: The tag to use for the image.
    :param apt_packages: A list of apt packages to install.
    :param yum_packages: A list of yum packages to install.
    :param conda_packages: A list of conda packages to install.
    :param pip_requirements: A list of pip requirements to install.
    :return: The metadata for the created image.
    """
    if isinstance(base_image, str):
        try:
            base_image = _KNOWN_BASE_IMAGES[base_image]
        except KeyError as e:
            raise ValueError(f"Unknown base image: {base_image}") from e
    for runner_layer in _KNOWN_RUNNER_LAYERS:
        if runner_layer.compatible_with(base_image):
            break
    else:
        raise ValueError(f"No compatible runner layer found for {base_image}")
    dockerfile = docker_templates.Dockerfile.from_image(base_image.from_arg())
    if apt_packages is not None:
        dockerfile = dockerfile.apply_apt_packages(apt_packages)
    if yum_packages is not None:
        dockerfile = dockerfile.apply_yum_packages(yum_packages)
    # Conda should precede pip.
    if conda_packages is not None:
        dockerfile = dockerfile.apply_conda_packages(conda_packages)
    if pip_requirements is not None:
        dockerfile = dockerfile.apply_pip_requirements(pip_requirements)
    dockerfile = dockerfile.apply_layer_tar(runner_layer.url)

    image = docker_wrappers.build_image(dockerfile.contents)
    image.tag(repository, tag=tag)
    client = docker.from_env()
    # https://github.com/docker/docker-py/issues/2226
    for line in client.images.push(repository, tag=tag, stream=True, decode=True):
        if "errorDetail" in line:
            raise RuntimeError(line["errorDetail"]["message"])
    # Command to get the digest without pulling the image.
    # https://stackoverflow.com/a/66267632/832056
    completed_process = subprocess.run(
        ["docker", "manifest", "inspect", f"{repository}:{tag}", "-v"],
        check=True,
        stdout=subprocess.PIPE,
    )
    digest = json.loads(completed_process.stdout)["Descriptor"]["digest"]

    return Image(
        repository=repository,
        tag=tag,
        digest=digest,
        builtin_framework=base_image.builtin_framework,
        builtin_framework_version=base_image.builtin_framework_version,
        python_version=base_image.python_version,
        cuda_version=base_image.cuda_version,
        has_conda=base_image.has_conda,
        dockerfile=dockerfile.contents,
    )
