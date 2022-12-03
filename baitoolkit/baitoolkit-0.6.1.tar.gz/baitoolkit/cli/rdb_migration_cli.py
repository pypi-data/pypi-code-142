# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
import argparse
import os

import click
from alembic import command
from alembic.config import Config as AlembicConfig

from baitoolkit.common.context_manager import global_ctx


class Config(AlembicConfig):
    def get_template_directory(self):
        package_dir = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(package_dir, 'templates')


def validate_directory(directory):
    """Return valid directory of migration."""
    if directory is None:
        root_path = global_ctx.app_root_path
        directory = os.path.join(root_path, 'migrations')
    return directory


def get_config(directory, x_arg=None, opts=None):
    config = Config(os.path.join(directory, 'alembic.ini'))
    config.set_main_option('script_location', directory)
    if config.cmd_opts is None:
        config.cmd_opts = argparse.Namespace()
    for opt in opts or []:
        setattr(config.cmd_opts, opt, True)
    if not hasattr(config.cmd_opts, 'x'):
        if x_arg is not None:
            setattr(config.cmd_opts, 'x', [])
            if isinstance(x_arg, list) or isinstance(x_arg, tuple):
                for x in x_arg:
                    config.cmd_opts.x.append(x)
            else:
                config.cmd_opts.x.append(x_arg)
        else:
            setattr(config.cmd_opts, 'x', None)
    file_tpl = config.get_section_option("alembic", "file_template")
    if file_tpl is not None:
        file_tpl = file_tpl.replace('%', '%%')
        version = global_ctx.app_version
        file_tpl = "v{}_{}".format(version, file_tpl)
        config.set_section_option("alembic", "file_template", file_tpl)
    return config


@click.group()
def rdb_migration_group():
    """Perform relationship database migrations."""
    context = click.get_current_context().obj


@rdb_migration_group.command(name="init")
@click.option('-d', '--directory', default=None,
              help='Migration script directory (default is "migrations")')
def init_cmd(directory):
    """Creates a new migration repository."""
    directory = validate_directory(directory)
    config = get_config(directory)
    command.init(config, directory, 'rdb_migration_cli')
    os.rename(os.path.join(directory, 'env.py.mako'), os.path.join(directory, 'env.py'))


@rdb_migration_group.command(name='revision')
@click.option('-d', '--directory', default=None,
              help='Migration script directory (default is "migrations")')
@click.option('-m', '--message', default=None, help='Revision message')
@click.option('--autogenerate', is_flag=True,
              help=('Populate revision script with candidate migration '
                    'operations, based on comparison of database to model'))
@click.option('--sql', is_flag=True,
              help=('Don\'t emit SQL to database - dump to standard output '
                    'instead'))
@click.option('--head', default='head',
              help=('Specify head revision or <branchname>@head to base new '
                    'revision on'))
@click.option('--splice', is_flag=True,
              help='Allow a non-head revision as the "head" to splice onto')
@click.option('--branch-label', default=None,
              help='Specify a branch label to apply to the new revision')
@click.option('--version-path', default=None,
              help='Specify specific path from config for version file')
@click.option('--rev-id', default=None,
              help=('Specify a hardcoded revision id instead of generating '
                    'one'))
def revision_db_cmd(directory, message, autogenerate, sql, head, splice, branch_label,
                    version_path, rev_id):
    """Create a new revision file."""
    directory = validate_directory(directory)
    config = get_config(directory)
    command.revision(config, message, autogenerate=autogenerate, sql=sql,
                     head=head, splice=splice, branch_label=branch_label,
                     version_path=version_path, rev_id=rev_id)


@rdb_migration_group.command(name="migrate")
@click.option('-d', '--directory', default=None,
              help='Migration script directory (default is "migrations")')
@click.option('-m', '--message', default=None, help='Revision message')
@click.option('--sql', is_flag=True,
              help=('Don\'t emit SQL to database - dump to standard output '
                    'instead'))
@click.option('--head', default='head',
              help=('Specify head revision or <branchname>@head to base new '
                    'revision on'))
@click.option('--splice', is_flag=True,
              help='Allow a non-head revision as the "head" to splice onto')
@click.option('--branch-label', default=None,
              help='Specify a branch label to apply to the new revision')
@click.option('--version-path', default=None,
              help='Specify specific path from config for version file')
@click.option('--rev-id', default=None,
              help=('Specify a hardcoded revision id instead of generating '
                    'one'))
@click.option('-x', '--x-arg', multiple=True,
              help='Additional arguments consumed by custom env.py scripts')
def migrate_cmd(directory, message, sql, head, splice, branch_label, version_path,
                rev_id, x_arg):
    """Autogenerate a new revision file (Alias for
    'revision --autogenerate')"""
    directory = validate_directory(directory)
    config = get_config(
        directory, opts=['autogenerate'], x_arg=x_arg)
    command.revision(config, message, autogenerate=True, sql=sql,
                     head=head, splice=splice, branch_label=branch_label,
                     version_path=version_path, rev_id=rev_id)


@rdb_migration_group.command(name="edit")
@click.option('-d', '--directory', default=None,
              help='Migration script directory (default is "migrations")')
@click.argument('revision', default='head')
def edit_cmd(directory, revision):
    """Edit a revision file"""
    directory = validate_directory(directory)
    config = get_config(directory)
    command.edit(config, revision)


@rdb_migration_group.command(name="merge")
@click.option('-d', '--directory', default=None,
              help='Migration script directory (default is "migrations")')
@click.option('-m', '--message', default=None, help='Merge revision message')
@click.option('--branch-label', default=None,
              help='Specify a branch label to apply to the new revision')
@click.option('--rev-id', default=None,
              help=('Specify a hardcoded revision id instead of generating '
                    'one'))
@click.argument('revisions', nargs=-1)
def merge_cmd(directory, message, branch_label, rev_id, revisions):
    """Merge two revisions together, creating a new revision file"""
    directory = validate_directory(directory)
    config = get_config(directory)
    command.merge(config, revisions, message=message,
                  branch_label=branch_label, rev_id=rev_id)


@rdb_migration_group.command(name="upgrade")
@click.option('-d', '--directory', default=None,
              help='Migration script directory (default is "migrations")')
@click.option('--sql', is_flag=True,
              help=('Don\'t emit SQL to database - dump to standard output '
                    'instead'))
@click.option('--tag', default=None,
              help=('Arbitrary "tag" name - can be used by custom env.py '
                    'scripts'))
@click.option('-x', '--x-arg', multiple=True,
              help='Additional arguments consumed by custom env.py scripts')
@click.argument('revision', default='head')
def upgrade_cmd(directory, sql, tag, x_arg, revision):
    """Upgrade to a later version"""
    directory = validate_directory(directory)
    config = get_config(directory, x_arg=x_arg)
    command.upgrade(config, revision, sql=sql, tag=tag)


@rdb_migration_group.command(name="downgrade")
@click.option('-d', '--directory', default=None,
              help='Migration script directory (default is "migrations")')
@click.option('--sql', is_flag=True,
              help=('Don\'t emit SQL to database - dump to standard output '
                    'instead'))
@click.option('--tag', default=None,
              help=('Arbitrary "tag" name - can be used by custom env.py '
                    'scripts'))
@click.option('-x', '--x-arg', multiple=True,
              help='Additional arguments consumed by custom env.py scripts')
@click.argument('revision', default='-1')
def downgrade_cmd(directory, sql, tag, x_arg, revision):
    """Revert to a previous version"""
    directory = validate_directory(directory)
    config = get_config(directory, x_arg=x_arg)
    if sql and revision == '-1':
        revision = 'head:-1'
    command.downgrade(config, revision, sql=sql, tag=tag)


@rdb_migration_group.command(name="show")
@click.option('-d', '--directory', default=None,
              help='Migration script directory (default is "migrations")')
@click.argument('revision', default='head')
def show_cmd(directory, revision):
    """Show the revision denoted by the given symbol."""
    directory = validate_directory(directory)
    config = get_config(directory)
    command.show(config, revision)


@rdb_migration_group.command(name="history")
@click.option('-d', '--directory', default=None,
              help='Migration script directory (default is "migrations")')
@click.option('-r', '--rev-range', default=None,
              help='Specify a revision range; format is [start]:[end]')
@click.option('-v', '--verbose', is_flag=True, help='Use more verbose output')
@click.option('-i', '--indicate-current', is_flag=True,
              help=('Indicate current version (Alembic 0.9.9 or greater is '
                    'required)'))
def history_cmd(directory, rev_range, verbose, indicate_current):
    """List changeset scripts in chronological order."""
    directory = validate_directory(directory)
    config = get_config(directory)
    command.history(config, rev_range, verbose=verbose, indicate_current=indicate_current)


@rdb_migration_group.command(name="heads")
@click.option('-d', '--directory', default=None,
              help='Migration script directory (default is "migrations")')
@click.option('-v', '--verbose', is_flag=True, help='Use more verbose output')
@click.option('--resolve-dependencies', is_flag=True,
              help='Treat dependency versions as down revisions')
def heads_cmd(directory, verbose, resolve_dependencies):
    """Show current available heads in the script directory"""
    directory = validate_directory(directory)
    config = get_config(directory)
    command.heads(config, verbose=verbose,
                  resolve_dependencies=resolve_dependencies)


@rdb_migration_group.command(name="branches")
@click.option('-d', '--directory', default=None,
              help='Migration script directory (default is "migrations")')
@click.option('-v', '--verbose', is_flag=True, help='Use more verbose output')
def branches_cmd(directory, verbose):
    """Show current branch points"""
    directory = validate_directory(directory)
    config = get_config(directory)
    command.branches(config, verbose=verbose)


@rdb_migration_group.command(name="current")
@click.option('-d', '--directory', default=None,
              help='Migration script directory (default is "migrations")')
@click.option('-v', '--verbose', is_flag=True, help='Use more verbose output')
def current_cmd(directory, verbose):
    """Display the current revision for each database."""
    directory = validate_directory(directory)
    config = get_config(directory)
    command.current(config, verbose=verbose)


@rdb_migration_group.command(name="stamp")
@click.option('-d', '--directory', default=None,
              help='Migration script directory (default is "migrations")')
@click.option('--sql', is_flag=True,
              help=('Don\'t emit SQL to database - dump to standard output '
                    'instead'))
@click.option('--tag', default=None,
              help=('Arbitrary "tag" name - can be used by custom env.py '
                    'scripts'))
@click.argument('revision', default='head')
def stamp_cmd(directory, sql, tag, revision):
    """'stamp' the revision table with the given revision; don't run any
    migrations"""
    directory = validate_directory(directory)
    config = get_config(directory)
    command.stamp(config, revision, sql=sql, tag=tag)
