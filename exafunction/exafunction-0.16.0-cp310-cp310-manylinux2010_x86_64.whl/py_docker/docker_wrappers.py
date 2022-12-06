# Copyright Exafunction, Inc.

"""Helper functions to invoke the Docker Python API."""

import contextlib
import logging
import os
import pathlib
from typing import Optional

import docker
from docker.client import DockerClient
from docker.models.images import Image


@contextlib.contextmanager
def _tmp_dockerfile(contents: str):
    path = pathlib.Path(os.getcwd()) / "exafunction.Dockerfile"
    path.write_text(contents, encoding="utf-8")
    try:
        yield {"path": str(path.parent), "dockerfile": "exafunction.Dockerfile"}
    finally:
        path.unlink()


def _build(client: DockerClient, **kwargs):
    try:
        return client.images.build(**kwargs)
    except docker.errors.BuildError as e:
        # The error message isn't logged by default.
        for line in e.build_log:
            if "stream" in line:
                logging.error(line["stream"].strip())
        raise


def build_image(dockerfile_contents: str, tag: Optional[str] = None) -> Image:
    """Build an image from a Dockerfile string."""
    client = docker.from_env()
    kwargs = {}
    if tag is not None:
        kwargs["tag"] = tag
    with _tmp_dockerfile(dockerfile_contents) as path_kwargs:
        image, _ = _build(client, **path_kwargs, **kwargs)
    if tag is not None:
        logging.info("Built new image with tag %s", image.tags[0])
        print(image.tags[0])
    else:
        logging.info("Built new image with id %s", image.id)
        print(image.id)
    return image
