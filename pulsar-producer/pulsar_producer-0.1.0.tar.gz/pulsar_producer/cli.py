import typer

from pathlib import Path
from typing import Optional

from pulsar_producer.producer import Producer


def main(pulsar_connection_file: Path = typer.Option(...), message_file: Path = typer.Option(...)):
    if pulsar_connection_file.exists() is False:
        print('"{}" does not exists.'.format(pulsar_connection_file))
        raise typer.Abort()

    if message_file.exists() is False:
        print('"{}" does not exists.'.format(message_file))
        raise typer.Abort()

    try:
        producer = Producer(pulsar_connection_file)
        producer.send_message(message_file)
    except Exception as error:
        print('Exception: {}'.format(error))
        raise typer.Abort()


def start():
    typer.run(main)
