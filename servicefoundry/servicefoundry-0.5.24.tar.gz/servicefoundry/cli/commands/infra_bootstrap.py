import rich_click as click

from servicefoundry.cli.const import COMMAND_CLS, GROUP_CLS
from servicefoundry.lib.infra.infra_bootstrap import Infra


@click.group(
    name="infra",
    cls=GROUP_CLS,
)
def infra():
    pass


@click.command(
    name="bootstrap",
    cls=COMMAND_CLS,
    help="Bootstrap truefoundry platform on an existing Kubernetes cluster",
)
@click.option(
    "--dry-run",
    is_flag=True,
    default=False,
)
def infra_bootstrap(dry_run: bool):
    infra_object = Infra(dry_run=dry_run)
    infra_object.provision()


def get_infra_command():
    infra.add_command(infra_bootstrap)
    return infra
