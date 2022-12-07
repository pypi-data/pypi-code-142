# system modules
import argparse
import functools
import json
import locale
import os
import re
import sys

# external modules
import evdev

# internal modules
from termkeymonitor.version import __version__


def find_keyboard_device():
    return sorted(
        evdev.list_devices(),
        key=lambda p: (
            ("keyboard" not in evdev.InputDevice(p).name),
            len(evdev.InputDevice(p).name),
        ),
    )[0]


def stop_on_keyboardinterrupt(decorated_fun):
    @functools.wraps(decorated_fun)
    def wrapper(*args, **kwargs):
        try:
            decorated_fun(*args, **kwargs)
        except KeyboardInterrupt:
            sys.exit(0)

    return wrapper


def key_pretty(name=None, code=None, show_code=False, keymap=dict()):
    suffix = f" ({code})" if show_code and code is not None else ""
    if s := keymap.get(name):
        return f"{s}{suffix}"
    if s := keymap.get(code):
        return f"{s}{suffix}"
    if s := keymap.get(str(code)):
        return f"{s}{suffix}"
    if name:
        return f"{name.removeprefix('KEY_')}{suffix}"
    if code:
        return str(code)
    return "?"


def tryint(x):
    try:
        return int(x)
    except Exception:
        return x


KEYMAPS = {
    "de": {
        "KEY_Y": "Z",
        "KEY_Z": "Y",
        53: "MINUS",
        26: "Ü",
        27: "+",
        43: "#",
        12: "ß",
        41: "^",
        40: "Ä",
        39: "Ö",
        86: "<",
        13: "ACCENT",
    }
}


def keymapargtype(value):
    try:
        if keymap := KEYMAPS.get(value):
            return keymap
        if os.path.exists(value):
            with open(value) as fh:
                keymap = json.load(fh)
        else:
            keymap = json.loads(value)
            return keymap
        keymap = {tryint(k): str(v) for k, v in keymap.items()}
    except Exception as e:
        raise argparse.ArgumentTypeError(
            """Specify either a JSON object like {"89":"mykey"} """
            f"or a path to a file with such JSON (error: {e})"
        )
    return keymap


default_keymap_name = re.sub(r"_.*$", r"", locale.getdefaultlocale()[0])


def make_argparser():
    parser = argparse.ArgumentParser("Show pressed keys")
    parser.add_argument(
        "-d",
        "--device",
        help="Input device to watch (e.g. /dev/input/event4)",
        type=evdev.InputDevice,
    )
    parser.add_argument(
        "-k",
        "--keymap",
        help="either directly JSON or path to "
        "JSON file with object mapping key "
        "codes or names to display strings "
        """(e.g. {"53":"MINUS","KEY_Z":"Y"}) """
        f"or the name of a build-in keymap ({' '.join(KEYMAPS)}). "
        f"Default locale name ({default_keymap_name}) is tried as default. "
        "(Tip: Add --show-code option or run "
        "'python -m evdev.evtest' to see codes and names)",
        type=keymapargtype,
        default=KEYMAPS.get(default_keymap_name, dict()),
    )
    parser.add_argument(
        "--show-code", help="Show keycode as well", action="store_true"
    )
    return parser
