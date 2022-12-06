"""Configuration represent."""
import json
from configparser import ConfigParser
from os import path

default = {
    "engine_url": ("https://downloads.tuxfamily.org/godotengine/{version}/"
                   "Godot_v{version}-stable_linux_headless.64.zip"),
    "templates_url": ("https://downloads.tuxfamily.org/godotengine/{version}/"
                      "Godot_v{version}-stable_export_templates.tpz"),
    "sha512": {
        "Godot_v3.5-stable_linux_headless.64.zip": (
            "df0ad2d5a0268725bb5d131eb5e9670bb0df50df6d41a2ed91db720675d9a1c72"
            "9278a9ef0eb04468c518412152a11e1711f653dbe900ebe1fd179d9861a9093"
        ),
        "Godot_v3.5-stable_export_templates.tpz": (
            "4e149be2bf7c3801a6e965c56ceca3258ddf2ea9206b33a5010eedb97693f710c"
            "d69fa568143747a6c884efe3ea5d7b74846804fa109a2efe80a47d66197238b"
        ),
    },
    "templates": {
        "HTML5": {
            "release": "webassembly_release.zip",
            "debug": "webassembly_debug.zip"
        },
        "Linux/X11": {
            "release": "linux_x11_64_release",
            "debug": "linux_x11_64_debug"
        },
        "Windows Desktop": {
            "release": "windows_64_release.exe",
            "debug": "windows_64_debug.exe"
        },
    },
    "custom": {
        "templates": False,
        "engine": True
    },
    "global": {
        "templates":
            path.expanduser("~/.local/share/godot/templates/{version}"),
        "engine": "godot"
    },
    "version": "3.5",
    "test_cmd": "{godot} -d -s --path {path} addons/gut/gut_cmdln.gd -gexit",
    "timeout": 900,
    "fail_regex": r"^\[Failed\]",
    "cache_dir": path.expanduser("~/.cache/gdbuild"),
    "engine_file": "Godot_v{version}-stable_linux_headless.64",
}


def save_default(path_dir: str):
    """Create default config in the given path."""
    full_path = path.join(path_dir, "gdbuild.json")
    with open(full_path, "w", encoding="utf-8") as config:
        config.write(json.dumps(default, indent=4))
        config.flush()
    print(f"Save default config: {full_path}")


def read(path_dir: str):
    """Read and return config file."""
    full_path = path.join(path_dir, "gdbuild.json")
    if not path.isfile(full_path):
        raise FileNotFoundError(f"{full_path} not exists")
    with open(full_path, "r", encoding="utf-8") as config:
        return json.loads(config.read())


def patch_presets(path_dir: str, version: str, clear=False):
    """Patch `export_presets.cfg` (add custom templates)."""
    presets_path = path.join(path_dir, "export_presets.cfg")
    presets = ConfigParser()
    presets.read(presets_path, encoding="utf-8")
    config = read(path_dir)
    for section in presets.sections():
        if not presets.has_option(section, "name"):
            continue
        name = presets.get(section, "name")[1:-1]
        if name not in config["templates"]:
            continue
        release_path = path.join(config["cache_dir"], version, "templates",
                                 config["templates"][name]["release"])
        debug_path = path.join(config["cache_dir"], version, "templates",
                               config["templates"][name]["debug"])
        if clear:
            release_path = ""
            debug_path = ""
        presets.set(section + ".options", "custom_template/release",
                    '"' + release_path + '"')
        presets.set(section + ".options", "custom_template/debug",
                    '"' + debug_path + '"')
    with open(presets_path, "w", encoding="utf-8") as presets_file:
        presets.write(presets_file)
