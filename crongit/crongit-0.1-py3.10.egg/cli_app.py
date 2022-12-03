from datetime import datetime
import os
import threading
import time
import click
import signal
import logging

from urllib.error import URLError

from crongit.client import Client
from crongit.dotfile import load_dotfile
from crongit.scheduler import SchedulerThread
from crongit.cli_output import info, success, err, warn, fatal
from crongit.server_handler import ServerThread

from tabulate import tabulate

from typing import Any, Dict, List, Optional


def _is_success(result: Dict[str, Any]) -> bool:
    messages: Optional[List[Dict[str, str]]] = result.get('messages', None)
    if not messages:
        return False

    for m in messages:
        severity: str = m.get('severity', 'info')
        if severity.startswith('err'):
            return False

    return True
    

def _display_result(result: Dict[str, Any]) -> None:
    messages: Optional[List[Dict[str, str]]] = result.get('messages', None)
    if not messages:
        err('Unknown error')
        return

    for msg in messages:
        severity: str = msg.get('severity', 'info')
        message = msg.get('message', '<Missing message>')

        fn = info if severity.startswith('info') \
        else success if severity.startswith('succ') \
        else warn if severity.startswith('warn') \
        else err

        fn(message)


@click.group
def cli() -> None:
    pass


@cli.command
@click.option('--reload-delay', type=int, default=5, show_default=True, help='Delay between config reloads.')
@click.option('--log-level', type=click.Choice(['DEBUG', 'INFO', 'WARN', 'ERROR'], case_sensitive=False), default='INFO', show_default=True, help='Log level.')
@click.option('--log-file', type=click.Path(file_okay=True), help='Logs to a file instead to stdout.')
@click.option('--dotfile', 'dotfile_path',
              type=click.Path(file_okay=True),
              default='$HOME/.crongit.conf',
              show_default=True, help='.crongit.conf location.')
def start(dotfile_path: str, reload_delay: int, log_level: str, log_file: Optional[str] = None) -> None:
    """Starts the main process.
    """

    logging.basicConfig(format='%(asctime)-5s %(levelname)-8s %(message)s',
                        filename=log_file,
                        level=getattr(logging, log_level.upper()))

    scheduler_thread = SchedulerThread(dotfile_path, reload_delay)
    server_thread = ServerThread (dotfile_path)

    def handle_signal(sig: int, frame: Any) -> None:
        name = signal.Signals(sig).name
        logging.info(f'{name} received.')

        if scheduler_thread.is_alive():
            logging.info('Stopping scheduler process...')
            scheduler_thread.stop()

        if server_thread.is_alive():
            logging.info('Stopping server process...')
            server_thread.stop()

    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    logging.info('Press Ctrl+C to stop...')

    scheduler_thread.start()
    server_thread.start()

    scheduler_thread.join()
    server_thread.join()


@cli.command()
@click.argument('path', type=click.Path(exists=True, dir_okay=True), nargs=1)
@click.option('--name', help='Repository friendly name.')
@click.option('--dotfile', 'dotfile_path',
              type=click.Path(file_okay=True),
              default='$HOME/.crongit.conf',
              show_default=True, help='.crongit.conf location.')
def add(path: str, name: Optional[str], dotfile_path: str):
    """Adds a repository to the .crongit.conf file.
    """

    dotfile = load_dotfile(dotfile_path)

    if not name:
        _, dirname = os.path.split(os.path.abspath(path))
        prompt_kwargs: Dict[str, str] = {}
        if dirname:
            prompt_kwargs['default'] = dirname
        while not name or not name.strip():
            name = click.prompt("Repository friendly name", **prompt_kwargs)

    client = Client(dotfile)
    try:
        result = client.make_request('add', path=path, name=name)
        _display_result(result)
    except URLError as e:
        fatal(str(e.reason))


@cli.command()
@click.option('--dotfile', 'dotfile_path',
              type=click.Path(file_okay=True),
              default='$HOME/.crongit.conf',
              show_default=True, help='.crongit.conf location.')
@click.argument('name')
def remove(dotfile_path: str, name: str):
    """Removes a repository from the .crongit.conf file.
    """

    dotfile = load_dotfile(dotfile_path)

    client = Client(dotfile)
    result = client.make_request('remove', name=name)
    _display_result(result)


@cli.command
@click.option('--add', 'autoadd', is_flag=True, default=False, help="Also, add the repository to the default .crongit.conf.")
@click.option('--dotfile', 'dotfile_path',
              type=click.Path(file_okay=True),
              default='$HOME/.crongit.conf',
              show_default=True, help='.crongit.conf location.')
@click.argument('path', type=click.Path(exists=True, dir_okay=True), default='.')
def init(autoadd: bool, dotfile_path: str, path: str):
    """Initializes a .crongit file in the specified path.
    """

    dotfile = load_dotfile(dotfile_path)
    client = Client(dotfile)
    result = client.make_request('init', path=path)
    _display_result(result)

    if _is_success(result) and autoadd:
        result = add(path, None, dotfile_path)
        _display_result(result)


@cli.command
@click.option('--dotfile', 'dotfile_path',
              type=click.Path(file_okay=True),
              default='$HOME/.crongit.conf',
              show_default=True, help='.crongit.conf location.')
def list(dotfile_path: str):
    """List all configured repositories.
    """

    dotfile = load_dotfile(dotfile_path)
    items = tuple((name, repo.get('path'))
                  for (name, repo) in dotfile.get_repos().items())
    print(tabulate(items, headers=('Name', 'Path'), tablefmt='simple'))


@cli.command
@click.option('--ini', 'ini_format', is_flag=True, default=False, help='Uses an output format suitable for config files')
@click.option('--dotfile', 'dotfile_path',
              type=click.Path(file_okay=True),
              default='$HOME/.crongit.conf',
              show_default=True, help='.crongit.conf location.')
@click.argument('name', type=str)
def show(ini_format, dotfile_path: str, name: str):
    """Show the effeective settings for a repository.
    """

    dotfile = load_dotfile(dotfile_path)
    items = dotfile.get_repo(name).items()
    if ini_format:
        for k,v in items:
            print(f'{k} = {v}')
    else:
        print(tabulate(items, headers=('Key', 'Value'), tablefmt='simple'))
