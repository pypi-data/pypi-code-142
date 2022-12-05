import click
from app.application import main

@click.command()
@click.argument('file_path')
def cli(file_path):
    main(file_path)


