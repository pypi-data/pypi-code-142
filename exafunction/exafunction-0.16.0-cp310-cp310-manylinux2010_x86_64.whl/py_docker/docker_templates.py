# Copyright Exafunction, Inc.

"""Utilities to generate Dockerfiles."""

from dataclasses import dataclass
import enum
import os
import shlex
import textwrap
from typing import List, Union


class _ExafunctionLayer(enum.Enum):
    RUNNER = enum.auto()
    LOCAL_E2E = enum.auto()


_KNOWN_LAYERS = {
    _ExafunctionLayer.RUNNER: "/app/exa/cmd/runner/runner",
    _ExafunctionLayer.LOCAL_E2E: "/app/exa/cmd/scheduler/local_e2e",
}


@dataclass
class Dockerfile:
    """Helper dataclass for type checking."""

    contents: str

    @staticmethod
    def from_image(image: str) -> "Dockerfile":
        """Initialize a Dockerfile from an existing image."""
        return Dockerfile(f"FROM {image}\n")

    def apply_layer_tar(self, url_or_relative_path: str) -> "Dockerfile":
        """Apply a layer tar archive to the Dockerfile."""
        # TODO(prem): Stricter validation of the argument.
        if "runner_layer" in url_or_relative_path:
            layer = _ExafunctionLayer.RUNNER
        elif "local_e2e_layer" in url_or_relative_path:
            layer = _ExafunctionLayer.LOCAL_E2E
        else:
            raise ValueError(
                "Unrecognized Exafunction layer type for archive"
                f" [{url_or_relative_path}]"
                " (name should contain runner_layer or local_e2e_layer)"
            )
        entrypoint = _KNOWN_LAYERS[layer]
        filename = os.path.basename(url_or_relative_path)
        if url_or_relative_path.startswith(("https://", "http://")):
            download_or_copy = f"ADD {url_or_relative_path} ."
        else:
            # Local archives are unpacked, so we can't use ADD.
            download_or_copy = f"COPY {url_or_relative_path} ."

        return Dockerfile(
            textwrap.dedent(
                f"""\
                {self.contents}
                WORKDIR /

                {download_or_copy}

                RUN tar -xzf {filename} && rm {filename}

                ENTRYPOINT {entrypoint}

                ENV RUNFILES_DIR={entrypoint}.runfiles
                """
            )
        )

    def apply_pip_requirements_txt(self, url_or_relative_path: str) -> "Dockerfile":
        """Apply a requirements.txt file to the Dockerfile."""
        if url_or_relative_path.startswith(("https://", "http://")):
            download_or_copy = (
                f"ADD {url_or_relative_path} ./exafunction_requirements.txt"
            )
        else:
            # Local archives are unpacked, so we can't use ADD.
            download_or_copy = (
                f"COPY {url_or_relative_path} ./exafunction_requirements.txt"
            )

        return Dockerfile(
            textwrap.dedent(
                f"""\
                {self.contents}
                {download_or_copy}

                RUN python3 -m pip install --no-cache-dir """
                "-r ./exafunction_requirements.txt"
                """ && rm ./exafunction_requirements.txt
                """
            )
        )

    def apply_run(self, command: Union[str, List[str]]) -> "Dockerfile":
        """Apply a RUN command to the Dockerfile."""
        if isinstance(command, str):
            command_str = command
        else:
            command_str = " ".join(command)  # TODO(prem): Backport shlex.join()
        return Dockerfile(
            textwrap.dedent(
                f"""\
                {self.contents}
                RUN {command_str}
                """
            )
        )

    def apply_pip_requirements(self, requirements: List[str]) -> "Dockerfile":
        """Apply a list of pip requirements to the Dockerfile."""
        return self.apply_run(
            shlex.split("python3 -m pip install --no-cache-dir") + sorted(requirements)
        )

    def apply_conda_packages(self, packages: List[str]) -> "Dockerfile":
        """Apply a list of conda packages to the Dockerfile."""
        return self.apply_run(
            shlex.split("conda install -y")
            + sorted(packages)
            + shlex.split("&& conda clean -y --all --force-pkgs-dirs")
        )

    def apply_yum_packages(self, packages: List[str]) -> "Dockerfile":
        """Apply a list of yum packages to the Dockerfile."""
        return self.apply_run(
            shlex.split("yum install -y")
            + sorted(packages)
            + shlex.split("&& yum clean all")
            + shlex.split("&& rm -rf /var/cache/yum/*")
        )

    def apply_apt_packages(self, packages: List[str]) -> "Dockerfile":
        """Apply a list of apt packages to the Dockerfile."""
        return self.apply_run(
            shlex.split("apt-get update && apt-get install -y")
            + sorted(packages)
            + shlex.split("&& apt-get clean")
            + shlex.split("&& rm -rf /var/lib/apt/lists/*")
        )
