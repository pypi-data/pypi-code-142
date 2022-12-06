import json
import os
import pathlib
from dataclasses import dataclass
from pathlib import Path
from time import time
from typing import Optional

import requests


@dataclass
class ProjectConfig:
    uid: str
    name: str


CONFIG_FILENAME = "databutton.json"


def get_databutton_config_path() -> Path:
    project_directory = pathlib.Path.cwd()
    retries = 1  # Increase to re-enable feature looking in parent directories or clean up code
    for _ in range(retries):
        filepath = project_directory / CONFIG_FILENAME
        if filepath.exists():
            return filepath
        project_directory = project_directory.parent
        if not project_directory.is_relative_to(pathlib.Path.home()):
            break
    raise FileNotFoundError(
        "Could not find databutton.json config file in parent directories."
    )


def get_project_directory() -> Path:
    return get_databutton_config_path().parent


def get_databutton_config() -> ProjectConfig:
    envvar = os.environ.get("DATABUTTON_PROJECT_ID")
    if envvar is not None:
        return ProjectConfig(name="env", uid=envvar)
    raise FileNotFoundError(
        "Could not find databutton config. Are you sure you've passed the DATABUTTON_PROJECT_ID environment variable?"
    )


def get_databutton_project_id() -> str:
    return get_databutton_config().uid


def get_api_url(project_id: str) -> str:
    u = os.environ.get("DATABUTTON_API_URL")
    return u or f"https://api.databutton.com/_projects/{project_id}/dbtn"


@dataclass
class LoginData:
    refreshToken: str
    uid: str


def get_databutton_login_info() -> Optional[LoginData]:
    if "DATABUTTON_TOKEN" in os.environ:
        return LoginData(refreshToken=os.environ["DATABUTTON_TOKEN"], uid="token")

    auth_path = get_databutton_login_path()
    auth_path.mkdir(exist_ok=True, parents=True)

    uids = [f for f in os.listdir(auth_path) if f.endswith(".json")]
    if len(uids) > 0:
        # Just take a random one for now
        with open(auth_path / uids[0]) as f:
            config = json.load(f)
            return LoginData(uid=config["uid"], refreshToken=config["refreshToken"])
    return None


def get_databutton_login_path():
    return Path(
        os.environ.get(
            "DATABUTTON_LOGIN_PATH", Path(Path.home(), ".config", "databutton")
        )
    )


FIREBASE_API_KEY = "AIzaSyAdgR9BGfQrV2fzndXZLZYgiRtpydlq8ug"

_cached_auth_token = None


def get_auth_token() -> str:
    global _cached_auth_token
    # This has a 15 minute cache
    if _cached_auth_token is not None and time() - _cached_auth_token[0] > 60 * 15:
        _cached_auth_token = None
    if _cached_auth_token is None:
        login_info = get_databutton_login_info()
        if login_info is None:
            raise Exception(
                "Could not find any login information."
                "\nAre you sure you are logged in?"
            )
        res = requests.post(
            f"https://securetoken.googleapis.com/v1/token?key={FIREBASE_API_KEY}",
            {"grant_type": "refresh_token", "refresh_token": login_info.refreshToken},
        )
        if not res.ok:
            raise Exception("Could not authenticate")
        json = res.json()
        _cached_auth_token = (time(), json["id_token"])
    return _cached_auth_token[1]
