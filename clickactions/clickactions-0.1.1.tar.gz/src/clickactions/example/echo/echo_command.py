import click
import pydevd
#
# pydevd.settrace(host='localhost', port=5678, stdoutToServer=True, stderrToServer=UnicodeTranslateError,
#                 suspend=False)

from clickactions import Command


class EchoCommand(Command):
    pass

    # def __init__(self, **kwargs):
    #     super(EchoAction, self).__init__(**kwargs)


@click.command(name="echo-actions", cls=EchoCommand)
@click.option('--message', required=True)
@click.pass_context
def command(ctx, message):
    print(f"Echo: {message}")
