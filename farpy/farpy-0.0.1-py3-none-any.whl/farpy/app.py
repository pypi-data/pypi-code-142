import click
import os


def inplace_replace(file, old, new):
    with open(file, 'r') as f:
        newText=f.read().replace(old, new)

    with open(file, "w") as f:
        f.write(newText)


@click.command()
@click.option('--path', '-p', type=str, help='file or folder path')
@click.option('--filetype', '-f', type=str, help='filetypes to change')
@click.option('--old', '-o', type=str, help='string to replace')
@click.option('--new', '-n', type=str, help='string to replace with')
def cli(path, filetype, old, new):
    if os.path.isfile(path):
        if filetype:
            if path.endswith(f'.{filetype}'):
                inplace_replace(path, old, new)
    if os.path.isdir(path):
        for dirs, subs, files in os.walk(path):
            for file in files:
                if file.endswith(f'.{filetype}'):
                    inplace_replace(os.path.join(path, dirs, file), old, new)

if __name__ == '__main__':
    pass