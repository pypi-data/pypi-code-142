import re
from pathlib import Path

import click


@click.group(help='Tools for files manipulation.')
def cli():
    ...


@cli.command(help='Perform file substitution with regular expression.')
@click.option('--pattern', '-p', help='The (Python) regex pattern to match.')
@click.option('--replace', '-r', help='The replacement string.')
@click.option('--inplace', '-i', is_flag=True, help='Edit files in place.')
@click.option('--echo', is_flag=True, help='Print the result even for inplace mode.')
@click.argument('filename')
def sub(
    pattern: str,
    replace: str,
    inplace: bool,
    echo: bool,
    filename: str,
):
    pattern = re.compile(pattern)
    filepath = Path(filename)

    content = filepath.read_text()
    new_content = pattern.sub(replace, content)

    if inplace:
        filepath.write_text(new_content)

    if not inplace or echo:
        print(new_content, end='', flush=True)


if __name__ == '__main__':
    cli()
