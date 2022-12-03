import sys
from platform import python_version

import click

from py_cover_letters.constants import BANNER
from py_cover_letters.utils import get_libreoffice_version


@click.command('about', help='About this application.')
def do_about():
    # check = u'\u2713'
    # not_valid = u'\u274C'

    libreoffice_version, is_valid = get_libreoffice_version()
    click.echo(BANNER)
    click.echo(f'Operating System: {sys.platform}')
    click.echo(f'Python : {python_version()}')
    click.echo(f'Libreoffice: {libreoffice_version}')
