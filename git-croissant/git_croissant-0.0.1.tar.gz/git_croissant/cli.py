#! /usr/bin/env python3


from typer import Typer

from .commands.clone import clone
from .commands.pousse import pousse
from .commands.tire import tire

app = Typer()


@app.callback(context_settings={"help_option_names": ["-h", "--help"]})
def main():
    ...


app.command()(clone)
app.command()(pousse)
app.command()(tire)

if __name__ == "__main__":
    app()
