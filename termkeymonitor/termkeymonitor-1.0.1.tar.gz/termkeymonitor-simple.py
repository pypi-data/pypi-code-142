# system modules
import argparse
import os
import sys
import textwrap

# external modules
import evdev

parser = argparse.ArgumentParser("Show pressed keys")
parser.add_argument(
    "-d",
    "--device",
    help="Input device to watch (e.g. /dev/input/event4)",
    type=evdev.InputDevice,
)


def find_keyboard_device():
    return sorted(
        evdev.list_devices(),
        key=lambda p: (
            ("keyboard" not in evdev.InputDevice(p).name),
            len(evdev.InputDevice(p).name),
        ),
    )[0]


def print_centered(s):
    s = textwrap.shorten(
        s, width=os.get_terminal_size().columns, placeholder="..."
    )
    s = s.center(os.get_terminal_size().columns - 1)
    sys.stdout.write(f"\r{s}")


def cli():
    args = parser.parse_args()
    if args.device is None:
        print_centered("\r🔎 Searching for input devices...")
        args.device = evdev.InputDevice(find_keyboard_device())
    print_centered(
        f"\r✅ Using input device {args.device.path!r} ({args.device.name!r})"
    )

    last_terminal_size = os.get_terminal_size()
    for event in args.device.read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            line = " ".join(
                name.removeprefix("KEY_")
                for name, code in args.device.active_keys(verbose=True)
            )
            print_centered(
                f"\r{{:^{os.get_terminal_size().columns}s}}".format(line)
            )


if __name__ == "__main__":
    cli()
