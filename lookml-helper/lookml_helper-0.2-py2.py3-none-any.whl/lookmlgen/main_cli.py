#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import click

from .gbqgen.main import *

HERE = os.path.abspath(os.path.dirname(__file__))

CMD_LINE_EXAMPLES = """EXAMPLES:
$ lookmlhelper ds-data-solutions-gbq dimensions-ai.data_analytics.clinical_trials

# For more option, run from Python directly
"""




@click.command()
@click.option('--examples', is_flag=True, help='Show some examples')
@click.option(
    '--billproject',
    '-b',
    help=
    'BILLING PROJECT: the GCP billing project to access resources.'
)
@click.option(
    '--dataset',
    '-d',
    help=
    'DATASET: a fully scopes GBQ dataset eg `dimensions-ai.data_analytics.clinical_trials`.'
)
@click.pass_context
def main_cli(ctx, billproject=None, dataset=None, examples=False):
    """lookmlhelper CLI.
Requires both a billproject and dataset to run. 
    """

    if examples:
        click.secho(CMD_LINE_EXAMPLES, fg="green")
        return

    if (billproject and dataset):
        run_gbq_extraction(
            gbq_billing_project=billproject,
            gbq_dataset=dataset,
        )

    else:
        click.echo(ctx.get_help())
        return


if __name__ == '__main__':
    main_cli()
