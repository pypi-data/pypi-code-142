import click
import pydevd

# pydevd.settrace(host='localhost', port=5678, stdoutToServer=True, stderrToServer=UnicodeTranslateError,
#                 suspend=False)

from clickactions import Commands


class EchoCommands(Commands):
    def __init__(self, **kwargs):
        super(EchoCommands, self).__init__(command_entry_points=
                                             {'clickactions.example.echo': None,
                                              'clickactions.command': '^(py-debug)$'},
                                           chain=True, **kwargs)


@click.command(cls=EchoCommands)
def commands():
    click.echo("EchoActions cli ran")
