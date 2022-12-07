# system modules
import sys
import functools

# internal modules
from termkeymonitor.version import __version__

# external modules
import evdev


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
