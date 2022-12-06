"""Serve aligned results for ezbee via zmq:5555."""
# pylint: disable=invalid-name
import json
import os
import sys
from pathlib import Path

# import signal
from signal import SIG_DFL, SIGINT, signal
from typing import Optional

import logzero
import typer
import zmq

# from ezbee.__main__.py
from ezbee import ezbee

# from ezbee.loadtext import loadtext
# from ezbee.text2lists import text2lists
from ezbee.gen_pairs import gen_pairs
from ezbee.save_xlsx_tsv_csv import save_xlsx_tsv_csv
from logzero import logger
from set_loglevel import set_loglevel

from dezmq import __version__, dezmq

logzero.loglevel(set_loglevel())

port_ = 5555

app = typer.Typer(
    name="dezmq",
    add_completion=False,
    help="dezmq help",
)


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{app.info.name} v.{__version__} -- {__doc__}")
        raise typer.Exit()


@app.command()
def main(
    version: Optional[bool] = typer.Option(  # pylint: disable=(unused-argument
        None,
        "--version",
        "-v",
        "-V",
        help="Show version info and exit.",
        callback=_version_callback,
        is_eager=True,
    ),
    port: Optional[int] = typer.Option(  # pylint: disable=(unused-argument
        None,
        "--port",
        "-p",
        help="Set port, default port 5555 (when -p is not present).",
    ),
):
    """Serve aligned results for ezbee via zmq at port 5555."""
    if port is None:
        port = port_

    # print(f"Listening (zmq.REP) on port: {port}. Press Ctrl-c to quit\n")
    logger.debug("Listening (zmq.REP) on port: %s. Press Ctrl-c to quit\n", port)


    context = zmq.Context()
    socket = context.socket(zmq.REP)  # type: ignore
    if socket is not None:
        socket.bind(f"tcp://*:{port}")
    else:
        logger.warning("Cant get a socket in 'context.socket(zmq.REP)'")
        raise Exception("socket error")
        
    # loop = True
    while True:
        _ = socket.recv()  # block/wait
        logger.debug("received: %s", _[:20])
        ...  # process message and send back result or break

        # res = {"res": f"{message}"}
        try:
            rec = json.loads(_.decode("utf8"))
            logger.debug("rec: %s, %s", rec, type(rec))
            
            # process
            lines1, lines2 = rec
            aset = ezbee(lines1, lines2)
            logzero.loglevel(set_loglevel())
            if aset:
                logger.debug("aset: %s...%s", aset[:3], aset[-3:])
                
            aligned_pairs = gen_pairs(lines1, lines2, aset)
            
            # socket.send(json.dumps(rec).encode("utf8"))
            socket.send(json.dumps(aligned_pairs).encode("utf8"))
            
            if rec in ['stop', 'quit']:
                logger.info(" received %s, exiting ", rec)
                break
        except Exception as exc:
            logger.error(exc)

if __name__ == "__main__":

    def signal_handler(sig, frame):
        print("You pressed Ctrl+C!")
        sys.exit(0)

    # signal(signal.SIGINT, signal_handler)
    signal(SIGINT, SIG_DFL)
    logger.info("To kill me: taskkill /f /pid %s", os.getpid())
    # signal.pause()

    app()
