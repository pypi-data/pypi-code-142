"""Godot wrapper."""
import re
import stat as stat_result
from enum import Enum, auto, unique
from hashlib import sha512
from os import chmod, makedirs, path, remove, rename, stat
from subprocess import CompletedProcess
from subprocess import run as run_process
from sys import exit as sys_exit
from urllib.request import urlopen
from zipfile import ZipFile

from godot_build.config import read as read_config


@unique
class TestType(Enum):
    """Type test running."""

    ALL = auto()
    INTERNAL = auto()
    COMMAND = auto()


class VersionManager():
    """Manage Godot engine versions (and export templates)."""

    def __init__(self, project_path: str):
        """Init.

        :param project_path: path to godot project with gdbuild.json
        """
        self.project_path = project_path
        self.config = read_config(project_path)

    def version(self, version: str) -> dict:
        """Get version data (path to engine and templates)."""
        version_path = path.join(self.config["cache_dir"], version)
        if not path.isdir(version_path):
            return {"templates": "", "engine": ""}
        engine_file = self.config["engine_file"].format(version=version)
        return {
            "templates": path.join(version_path, "templates"),
            "engine": path.join(version_path, engine_file),
        }

    def add_version(self, version: str):
        """Add (download) new version Godot engine and templates."""
        version_path = path.join(self.config["cache_dir"], version)
        version_data = self.version(version)
        if self.config["custom"]["engine"] and not path.isfile(
                version_data["engine"]):
            if not path.isdir(version_path):
                makedirs(version_path)
            zip_path = self._download_engine(version)
            print(f"Extract {zip_path}")
            self._extract(zip_path, version_path)
            remove(zip_path)
            version_data = self.version(version)
            engine_stat = stat(version_data["engine"])
            chmod(version_data["engine"],
                  engine_stat.st_mode | stat_result.S_IEXEC)
        if self.config["custom"]["templates"] and not path.isdir(
                version_data["templates"]):
            if not path.isdir(version_path):
                makedirs(version_path)
            zip_path = self._download_templates(version)
            print(f"Extract {zip_path}")
            self._extract(zip_path, version_path)
            remove(zip_path)
        templates_dir = self.config["global"]["templates"].format(
            version=version)
        if not self.config["custom"]["templates"] and not path.isdir(
                templates_dir):
            url = self.config["engine_url"].format(version=version)
            save_path = path.dirname(templates_dir)
            zip_path = self._download(url, save_path)
            print(f"Extract {zip_path}")
            self._extract(zip_path, save_path)
            remove(zip_path)
            rename(path.join(save_path, "templates"),
                   path.join(save_path, version))
        print(f"Version {version} success add!")

    def _get_sha512(self, file_path: str) -> str:
        checksum = sha512()
        with open(file_path, "rb") as file:
            while file.readable():
                data = file.read(1024)
                if not data:
                    break
                checksum.update(data)
        return checksum.hexdigest()

    def _download(self, url: str, save_path: str) -> str:
        name = path.basename(url)
        path_cache = path.join(save_path, name)
        if path.isfile(path_cache):
            if self._get_sha512(path_cache) == self.config["sha512"][name]:
                return path_cache
            remove(path_cache)
        checksum = sha512()
        print(f"Download: {url}")
        with urlopen(url) as dist_file:
            with open(path_cache, "wb") as cache_file:
                while dist_file.readable():
                    data = dist_file.read(1024)
                    if not data:
                        break
                    cache_file.write(data)
                    checksum.update(data)
                cache_file.flush()
        if checksum.hexdigest() != self.config["sha512"][name]:
            raise AssertionError(f"wrong checksum for {name}")
        print(f"Done: {path_cache}")
        return path_cache

    def _download_engine(self, version: str) -> str:
        url = self.config["engine_url"].format(version=version)
        save_path = path.join(self.config["cache_dir"], version)
        return self._download(url, save_path)

    def _download_templates(self, version: str) -> str:
        url = self.config["templates_url"].format(version=version)
        save_path = path.join(self.config["cache_dir"], version)
        return self._download(url, save_path)

    def _extract(self, file: str, to_path: str):
        with ZipFile(file, "r") as archive:
            archive.extractall(to_path)


class GodotRunner():
    """Run util."""

    def __init__(self, project_path: str):
        """Init.

        :param project_path: path to godot project with gdbuild.json
        """
        self.project_path = project_path
        self.config = read_config(project_path)

    def run(self, cmd) -> CompletedProcess:
        """Run godot.

        :param cmd: list arguments
        """
        print("Run: " + " ".join(str(arg) for arg in cmd))
        timeout = self.config["timeout"]
        if timeout == 0:
            timeout = None
        completed = run_process(cmd,
                                capture_output=True,
                                timeout=timeout,
                                text=True)
        return completed

    def format(self, command: str) -> str:
        """Replace `{godot}` and `{path}` to current values."""
        engine = self.config["global"]["engine"]
        if self.config["custom"]["engine"]:
            vers_manager = VersionManager(self.project_path)
            engine = vers_manager.version(self.config["version"])["engine"]
        return command.format(godot=engine, path=self.project_path)


class TestRunner(GodotRunner):
    """Test util."""

    def run_test_cmd(self):
        """Run test command."""
        cmd = self.format(self.config["test_cmd"])
        completed = self.run(cmd.split(" "))
        failed = False
        for line in completed.stdout.splitlines():
            print(line)
            if re.match(self.config["fail_regex"], line.strip()):
                failed = True
        if failed or completed.returncode != 0:
            sys_exit(1)

    def run_test_internal(self):
        """Run internal test (check project files)."""
        files = (
            "project.godot",
            "export_presets.cfg",
        )
        failed = False
        for file_name in files:
            file_path = path.join(self.project_path, file_name)
            if path.isfile(file_path):
                print(f"[Passed] {file_path} exists")
            else:
                print(f"[Failed] {file_path} exists")
                failed = True
        if failed:
            sys_exit(1)

    def run_test(self, test: TestType):
        """Run test by enum."""
        if test == TestType.COMMAND:
            self.run_test_cmd()
        elif test == TestType.INTERNAL:
            self.run_test_internal()
        else:
            self.run_test_cmd()
            self.run_test_internal()
