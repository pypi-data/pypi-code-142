# system modules
import argparse
import os
import sys
import textwrap

# internal modules
from termkeymonitor import (
    find_keyboard_device,
    stop_on_keyboardinterrupt,
    make_argparser,
    key_pretty,
)

# external modules
import evdev


def print_centered(s):
    s = textwrap.shorten(
        s, width=os.get_terminal_size().columns, placeholder="..."
    )
    s = s.center(os.get_terminal_size().columns - 1)
    sys.stdout.write(f"\r{s}")


@stop_on_keyboardinterrupt
def cli():
    parser = make_argparser()
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
                key_pretty(
                    name=name,
                    code=code,
                    keymap=args.keymap,
                    show_code=args.show_code,
                )
                for name, code in args.device.active_keys(verbose=True)
            )
            print_centered(line)


if __name__ == "__main__":
    cli()
