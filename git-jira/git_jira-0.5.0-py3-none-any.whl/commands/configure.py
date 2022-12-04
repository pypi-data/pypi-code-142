import click
from pick import pick
from git_jira.config import Config
from git_jira.utils import INDICATOR


def pick_default_branch_format():
    option, _ = pick(
        ["Yes", "No, use default `issue_key-issue_summary`"],
        "Do you want to specify a default branch name format?",
        indicator=INDICATOR,
    )
    if option == "Yes":
        return [
            click.prompt(
                "Define a branch format using issue_key and issue_summary as placeholders",
                type=str,
            )
        ]
    else:
        return ["issue_key-issue_summary"]


def pick_additional_formats():
    option, _ = pick(
        ["Yes", "No, just use default"],
        "Do you want to specify additional branch name formats?",
        indicator=INDICATOR,
    )
    if option == "Yes":
        additional_branch_formats = []
        add_another = "Yes"
        while add_another == "Yes":
            additional_branch_formats.append(
                click.prompt(
                    "Define a branch format using issue_key and issue_summary as placeholders",
                    type=str,
                )
            )
            add_another, _ = pick(
                ["Yes", "No, I'm done"], "Do you want another one?", indicator=INDICATOR
            )
        return additional_branch_formats
    else:
        return []


def define_branch_formats():
    branch_formats = pick_default_branch_format()
    additional_formats = pick_additional_formats()
    if additional_formats:
        branch_formats.extend(additional_formats)
    return branch_formats


def jira_config_input():
    config = dict()
    config["server_url"] = click.prompt("Jira server url", type=str)
    config["username"] = click.prompt("Jira username", type=str)
    config["api_token"] = click.prompt("Jira API token", type=str)
    config["default_project_key"] = click.prompt("Default project", type=str)
    config["branch_formats"] = define_branch_formats()
    return config


@click.command()
def configure():
    click.echo("Welcome to git-jira. Let's generate your config file...")
    config = {"jira": jira_config_input()}
    click.echo(
        f"A config file with the following params will be created at {Config().path} \n"
    )
    click.echo(f"{Config().str_content(config)}")
    if click.confirm("Do you want to continue?"):
        Config().change(config)
        click.echo(f"Config file successfully created.")
        click.echo("Thanks for using git-jira!")
    else:
        click.echo(f"Configuration aborted.")
