# system modules
import os

# internal modules
import termkeymonitor
from termkeymonitor import (
    stop_on_keyboardinterrupt,
    find_keyboard_device,
    make_argparser,
    key_pretty,
)

# external modules
import evdev
from rich.live import Live
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.layout import Layout


console = Console()


@stop_on_keyboardinterrupt
def cli():
    parser = make_argparser()
    args = parser.parse_args()

    layout = Layout(name="root")
    with Live(layout, screen=True, transient=True) as live:

        def update(text):
            c = Align(
                Text(text, style="bold"),
                align="center",
                vertical="middle",
            )
            layout["root"].update(
                c
                if os.get_terminal_size().lines < 3
                else Panel(
                    c,
                    title="⌨️  Keyboard",
                ),
            )
            live.refresh()

        if args.device is None:
            update("🔎 Searching for input devices...")
            args.device = evdev.InputDevice(find_keyboard_device())
        update(
            f"✅ Using input device {args.device.path!r} "
            f"({args.device.name!r})",
        )
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
                update(line)


if __name__ == "__main__":
    cli()
