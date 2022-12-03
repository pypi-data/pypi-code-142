import click

from py_cover_letters.config import ConfigurationManager


@click.command(help='Configure the application.')
@click.argument('sub_command', required=False)
@click.option('--overwrite', is_flag=True, default=False, help="Overwrite the configuration file.")
def config(sub_command, overwrite):
    """Configure the application. Sub commands:
    show: shows current configuration.
    delete: deletes current configuration."""
    if sub_command is None:
        click.echo('Configuration')
        config_manager = ConfigurationManager()
        do_configuration(config_manager, overwrite)
    elif sub_command == 'show':
        show()
    else:
        click.echo(f'sub command {sub_command}')


def do_configuration(config_manager: ConfigurationManager, overwrite: bool):
    configuration = config_manager.get_sample_config()
    if config_manager.config_file.exists() and not overwrite:
        click.echo(f'The configuration already exists ({config_manager.config_file}). Use the --overwrite flag.')
        return
    if config_manager.config_file.exists() and overwrite:
        backup_filename = config_manager.backup()
        click.echo(f'Backup of the current config file was made {backup_filename}')
        configuration = config_manager.get_configuration()
    new_configuration = configuration.copy()
    for key, key_conf in configuration.items():
        click.echo(f'[{key.upper()}]')
        for sub_key, sub_key_conf in key_conf.items():
            prompt_text = f'{sub_key.replace("_", " ")}'
            new_key = click.prompt(prompt_text, default=sub_key_conf)
            new_configuration[key][sub_key] = new_key
    config_manager.write_configuration(new_configuration, over_write=True)


def show():
    click.secho('Show subcommand is not implemented yet.', fg='red')


def delete(config_manager: ConfigurationManager):
    click.secho('Delete subcommand is not implemented yet.', fg='red')
