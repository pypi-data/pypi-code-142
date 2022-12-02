import logging
import click

from .version import __version__
from .decoder import Decoder

logging.basicConfig()
log = logging.getLogger(__name__)


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.version_option(version=__version__)
@click.option("-f", "--file", type=click.Path(exists=True), help="Path to the file to be processed")
@click.option("-v", "--verbose", is_flag=True, help="Enable verbose logging")
@click.option("-b", "--blur", help="Type of deblur to use: blind or non-blind", default="non-blind")
@click.option("-s", "--save", help="Path to save the processed image")
@click.option("-d", "--decode", is_flag=True, help="Enable decoding of the image", default=True)
def qqr(file, verbose, blur, save, decode):
    """qqr: a command line tool to query qrcode from terminal."""
    if file is not None:
        Decoder(file, verbose, blur, saveFile=save, decode=decode)


if __name__ == "__main__":
    qqr()
