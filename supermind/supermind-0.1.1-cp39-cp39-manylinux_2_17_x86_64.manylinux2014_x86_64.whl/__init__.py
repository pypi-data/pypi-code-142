import click
import pkgutil


__version__ = pkgutil.get_data(__package__, 'VERSION.txt').decode('ascii').strip()


@click.group()
def cli():
    pass
