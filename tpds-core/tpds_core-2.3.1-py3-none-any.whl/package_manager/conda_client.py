from __future__ import annotations

"""
Conda/Anaconda Package Manager Client and Tools
"""

import json
import os
from typing import Any, Optional, Sequence, Union

from packaging import version

# Trust Platform Modules
from tpds.settings import TrustPlatformSettings

from .client_model import PackageManagerClient
from .data_models import (
    CondaAboutModel,
    CondaInfoModel,
    CondaPackageDetails,
    CondaSearchModel,
    PackageDependencies,
    PackageDetails,
)


# While it should likely be safe to grab the last entry in the list it appears that the list is
# appended when a new package is uploaded which means that patch to a previous version would get
# precedence over major/minor update that was published prior
def _conda_get_latest(packages: Sequence[CondaPackageDetails]) -> CondaPackageDetails:
    latest = None
    latest_ver = version.parse("0.0.0")
    latest_build = 0
    for p in packages:
        if p.version > latest_ver or (p.version == latest_ver and p.build_number > latest_build):
            latest = p
            latest_ver = p.version
            latest_build = p.build_number
    return latest


def _conda_find_channel(channel: str) -> str:
    if "/" in channel:
        parts = channel.split("/")
        if parts[-1] in [
            "noarch",
            "win-32",
            "win-64",
            "linux-32",
            "linux-64",
            "osx-64",
            "osx-arm64",
        ]:
            return parts[-2]
        else:
            return parts[-1]
    return channel


class CondaPackageClient(PackageManagerClient):
    """
    Interact with the Anaconda packaging system
    """

    def __init__(self, channel_list: Optional[Sequence[str]] = None, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._installed: dict[str, CondaPackageDetails] = {}
        self._available: dict[str, CondaPackageDetails] = {}
        if channel_list:
            self._channels = channel_list
        else:
            self._channels = TrustPlatformSettings().settings.conda_channels

        self._info = self._conda_info()

    def login(self, username: str, password: str, hostname: str, **kwargs) -> None:
        """
        Provide the user credentials for logging into the system
        """
        cmd = [
            "anaconda",
            "login",
            "--username",
            username,
            "--password",
            password,
            "--hostname",
            hostname,
        ]
        outs, code = self._proc.run_cmd(
            cmd, timeout=60, err_handling=self._proc.CAPTURE, log_args=False, **kwargs
        )
        self._log.log(outs)
        if code != 0:
            raise ValueError("Unable to login")

    def logout(self, **kwargs) -> None:
        """
        Log out of the system
        """
        cmd = ["anaconda", "logout"]
        self._proc.run_cmd(cmd, timeout=120, err_handling=self._proc.CAPTURE, **kwargs)

    def is_logged_in(self, **kwargs) -> Union[str, None]:
        """
        Check if anyone is logged in Anacaonda prompt
        Requires active internet connection.
        """
        cmd = ["anaconda", "whoami"]
        outs, _ = self._proc.run_cmd(cmd, timeout=120, err_handling=self._proc.CAPTURE, **kwargs)

        if "Username" in outs:
            for line in outs.splitlines():
                if "Username" in line:
                    return line.replace("Username: ", "").strip()
        return None

    def _conda_info(self, **kwargs) -> CondaInfoModel:
        """
        Update conda installation info
        """
        cmd = ["conda", "info", "--json"]
        outs, _ = self._proc.run_cmd(cmd, timeout=120, err_handling=self._proc.CAPTURE, **kwargs)
        return CondaInfoModel(**json.loads(outs))

    def _conda_show(self, channel: str = None, pattern: str = "tpds*", **kwargs) -> None:
        """
        Conda search - retrieve information based on the channel and conda search spec
        Fetches information about a object specified
        """
        cmd = ["conda", "search", "--json"]
        cmd += self._conda_arguments(pattern, channel=channel)
        outs, errorcode = self._proc.run_cmd(
            cmd, timeout=120, err_handling=self._proc.CAPTURE, **kwargs
        )
        if errorcode:
            self._log.log(outs.replace("\n", ""))
            return []
        else:
            searchdata = CondaSearchModel.parse_obj({"packages": json.loads(outs)})
            return [_conda_get_latest(v) for v in searchdata.packages.values()]

    def _conda_read_info(self, data: CondaPackageDetails, **kwargs) -> Union[CondaAboutModel, None]:
        """
        Load package data that is included in the about.json file - this is where we get
        dependency information
        """
        for d in self._info.envs:
            # Build the package directory based on the environment paths
            info_path = os.path.join(
                d, "pkgs", f"{data.name}-{data.version}-{data.build_string}", "info", "about.json"
            )
            if os.path.exists(info_path):
                try:
                    return CondaAboutModel.parse_file(info_path)
                except Exception as e:
                    self._log.log(f"Parsing failed for {info_path}")

    def _conda_arguments(
        self, packages: Union[str, Sequence[str]], channel: Optional[str] = None
    ) -> Sequence[str]:
        """
        Create argument list for conda commands based on parameters and configuration data
        """
        if channel:
            channels = [channel] if isinstance(channel, str) else channel
        elif len(self._channels):
            channels = self._channels
        else:
            channels = []

        if channels:
            args = ["--override-channels"]
            for c in channels:
                args += ["-c", c]
        else:
            args = []

        if packages is None:
            raise AttributeError("No packages were specified")
        elif isinstance(packages, str):
            args += [packages]
        else:
            args += packages

        return args

    def _conda_download(
        self, packages: Union[str, Sequence[str]], channel: Optional[str] = None, **kwargs: Any
    ) -> None:
        """
        Download the package first before actually installing it so we can check the info for dependencies
        """
        cmd = ["conda", "install", "--quiet", "--freeze-installed", "--download-only", "--json"]
        cmd += self._conda_arguments(packages, channel)

        outs, _ = self._proc.run_cmd(cmd, timeout=120, err_handling=self._proc.CAPTURE, **kwargs)
        self._log.log(outs)

    def _conda_install(
        self, packages: Union[str, Sequence[str]], channel: Optional[str] = None, **kwargs: Any
    ) -> None:
        """
        Install conda packages
        """
        cmd = ["conda", "install", "-y", "--quiet", "--freeze-installed"]
        cmd += self._conda_arguments(packages, channel)

        outs, _ = self._proc.run_cmd(cmd, timeout=120, err_handling=self._proc.CAPTURE, **kwargs)
        self._log.log(outs)

    def _conda_upgrade(
        self, packages: Union[str, Sequence[str]], channel: Optional[str] = None, **kwargs: Any
    ) -> None:
        """
        Upgrade packages to the latest compatable version
        """
        cmd = ["conda", "update", "-y", "--quiet", "--freeze-installed"]
        cmd += self._conda_arguments(packages, channel)

        outs, _ = self._proc.run_cmd(cmd, timeout=120, err_handling=self._proc.CAPTURE, **kwargs)
        self._log.log(outs)

    def update_local(self, **kwargs: Any) -> None:
        """
        Update the packaging information
        """
        cmd = ["conda", "list", "--json"]
        outs, rc = self._proc.run_cmd(cmd)
        if rc == 0 and outs:
            for package in json.loads(outs):
                details = CondaPackageDetails(**package)
                details.about = self._conda_read_info(details, **kwargs)
                self._installed[details.name] = details

    def update_remote(self, **kwargs: Any) -> None:
        """
        Retrieve the list of available packages and their versions
        """

        def match_channel(chan1, chan2):
            return _conda_find_channel(chan1) == _conda_find_channel(chan2)

        for chan in filter(lambda c: "microchip" in c, self._channels):
            for item in self._conda_show(channel=[chan], **kwargs):
                if item.name not in self._installed or match_channel(
                    item.channel, self._installed[item.name].channel
                ):
                    if (
                        item.name not in self._available
                        or item.version > self._available[item.name].version
                    ):
                        item.about = self._conda_read_info(item, **kwargs)
                        self._available[item.name] = item

    def install(self, packages: Union[str, Sequence[str]], **kwargs) -> None:
        """
        Install the selected packages and their dependencies
        """
        if isinstance(packages, str):
            packages = [packages]

        for package in packages:
            inst = self._installed.get(package)
            avail = self._available.get(package)
            if inst and avail:
                self._conda_upgrade(package, avail.channel, **kwargs)
            elif avail:
                self._conda_install(package, avail.channel, **kwargs)
        self.update_local()

    def upgrade(self, packages: Union[str, Sequence[str]], **kwargs) -> None:
        """
        Upgrade the selected packages to the latest versions
        """
        if isinstance(packages, str):
            packages = [packages]

        for package in packages:
            info = self._available.get(package)
            if info:
                self._conda_upgrade(package, info.channel, **kwargs)
        self.update_local()

    def update_dependency_list(
        self, packages: Union[str, Sequence[str]], channel: Optional[str] = None, **kwargs: Any
    ) -> PackageDependencies:
        """
        Dependencies are listed as part of additional metadata so we need to retrieve
        that information first before we execute additional steps
        """
        if isinstance(packages, str):
            packages = [packages]

        dependencies = PackageDependencies()
        self._conda_download(packages, channel, **kwargs)

        for item in packages:
            details = self._available.get(item)
            details.about = self._conda_read_info(details)
            try:
                dependencies.conda += details.about.extra.tpds.required.conda
            except:
                pass
            try:
                dependencies.pypi += details.about.extra.tpds.required.pypi
            except:
                pass

        dependencies.conda = list(set(dependencies.conda))
        dependencies.pypi = list(set(dependencies.pypi))

        return dependencies

    def _package_details(
        self, package: CondaPackageDetails, installed: bool = False
    ) -> PackageDetails:
        details = PackageDetails(
            name=package.name, channel=package.channel, license=package.license
        )
        if installed:
            details.installed = package.version
        else:
            details.latest = package.version

        if package.about:
            try:
                details.dependencies = package.about.extra.tpds.required
            except AttributeError:
                pass
            try:
                details.extras = package.about.extra.tpds.optional
            except AttributeError:
                pass
        return details

    def _filter_packages(
        self, packages: dict[str, CondaPackageDetails], pattern: str
    ) -> Sequence[CondaPackageDetails]:
        filtered = filter(lambda x: pattern in x, packages.keys())
        result = {}
        for x in filtered:
            if package := packages.get(x, None):
                if package.channel != "pypi":
                    result[x] = package
        return result.values()

    def get_dependencies(self, pattern: str = "tpds") -> Sequence[PackageDetails]:
        """
        Get a list of dependencies we need to watch
        """
        packages = self._installed
        filtered = filter(lambda x: pattern in x, packages.keys())
        result = {}
        for x in filtered:
            package = packages.get(x)
            try:
                for d in package.about.extra.tpds.required.conda:
                    if d in packages:
                        result[d] = packages.get(d)
            except:
                pass
            try:
                for d in package.about.extra.tpds.required.pypi:
                    if d in packages:
                        result[d] = packages.get(d)
            except:
                pass
        return [self._package_details(v, True) for v in result.values()]

    def get_installed_packages(self, pattern: str = "tpds") -> Sequence[PackageDetails]:
        """
        Get a list of installed tpds packages
        """
        return [
            self._package_details(v, True) for v in self._filter_packages(self._installed, pattern)
        ]

    def get_available_packages(self, pattern: str = "tpds") -> Sequence[PackageDetails]:
        """
        Get a list of all available packages that can be installed
        """
        return [self._package_details(v) for v in self._filter_packages(self._available, pattern)]


__all__ = ["CondaPackageClient"]
