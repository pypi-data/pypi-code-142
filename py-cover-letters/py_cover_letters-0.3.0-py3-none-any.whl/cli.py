"""Console script for py_cover_letters."""

import click

from . import __version__ as current_version
from .cli_commands.about_cmd import do_about
from .cli_commands.configuration_cmd import config


@click.group()
@click.version_option(version=current_version)
def main():
    pass


@click.command(help='Create cover letters from master Excel file.')
@click.option('--all', 'create_all', is_flag=True, default=True, help='Create all cover letters.')
def create():
    click.echo('Creating cover letters')


@click.command(help='Email cover letters.')
@click.option('--all', 'email_all', is_flag=True, default=True, help='Email all the unsent cover letters.')
@click.option('--confirm', is_flag=True, default=True, help='Confirmation before sending the email.')
def email(email_all: bool, confirm: bool):
    click.echo('Email cover letters')


main.add_command(config)
main.add_command(create)
main.add_command(email)
main.add_command(do_about)
# main.add_command(do_sync)

if __name__ == "__main__":
    main()  # pragma: no cover
