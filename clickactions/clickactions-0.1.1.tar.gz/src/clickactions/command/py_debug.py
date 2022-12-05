import click
import clickactions
import pydevd


@click.command(cls=clickactions.Command)
@click.option('--off', is_flag=True)
@click.option('--host', default='localhost')
@click.option('--port', type=int, default=5678)
@click.option('--out', is_flag=True)
@click.option('--err', is_flag=True)
@click.option('--suspend', is_flag=True)
def command(off, host, port, out, err, suspend):
    if off:
        pydevd.stoptrace()
    else:
        pydevd.settrace(host=host, port=port, stdoutToServer=out, stderrToServer=err,
                        suspend=suspend)
