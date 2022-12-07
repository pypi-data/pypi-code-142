# system modules
import argparse
import os
import sys
import threading

# internal modules
from termkeymonitor import find_keyboard_device, make_argparser

# external modules
import evdev
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widget import Widget


class KeyDisplay(Widget):
    def __init__(self, device, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.device = device
        self.keythread = threading.Thread(target=self.watch_keys)

    text = reactive("")

    def watch_keys(self) -> None:
        # self.app.log(f"Hi from thread")
        for event in self.device.read_loop():
            # self.app.log(f"Key event!")
            if event.type == evdev.ecodes.EV_KEY:
                line = " ".join(
                    name.removeprefix("KEY_")
                    for name, code in self.device.active_keys(verbose=True)
                )
                # self.app.log(f"{line = }")
                self.text = line

    def on_mount(self) -> None:
        self.app.log("Starting key watcher thread")
        self.keythread.start()

    def render(self) -> str:
        return f"{self.text}"


class KeyApp(App):
    def __init__(self, device=None, *args, **kwargs):
        App.__init__(self, *args, **kwargs)
        if device is None:
            self.device = evdev.InputDevice(find_keyboard_device())
        else:
            self.device = device

    def compose(self) -> ComposeResult:
        yield KeyDisplay(self.device)


def cli():
    parser = make_argparser()
    args = parser.parse_args()
    if args.device is None:
        print("🔎 Searching for input devices...")
        args.device = evdev.InputDevice(find_keyboard_device())
    print(f"✅ Using input device {args.device.path!r} ({args.device.name!r})")
    app = KeyApp()
    app.device = args.device
    app.run()


if __name__ == "__main__":
    cli()
