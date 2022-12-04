import click
from pick import pick
from git_jira.config import Config
from git_jira.jira import JiraIssue, JiraMetaIssue
from git_jira.git import GitBranch
from git_jira.utils import INDICATOR
from git_jira.commands.issue import assign_issue


def prompt_field(field):
    if field["type"] == "string":
        return click.prompt(field["name"], type=str)
    elif field["type"] == "number":
        return click.prompt(field["name"], type=float)
    elif field["type"] == "option":
        option, _ = pick(
            [opt["value"] for opt in field["options"]],
            field["name"],
            indicator=INDICATOR,
        )
        click.echo(f"{field['name']}: {option}")
        return {"value": option}
    elif field["type"] == "array":
        response = pick(
            [opt["value"] for opt in field["options"]],
            f"{field['name']} (press SPACE to select, ENTER to continue",
            multiselect=True,
            min_selection_count=1,
            indicator=INDICATOR,
        )
        click.echo(f"{field['name']}: {', '.join([option[0] for option in response])}")
        return [{"value": option[0]} for option in response]


def issue_fields_input():
    meta_issue = JiraMetaIssue()
    fields = dict()
    click.echo("Fill in the required fields")
    fields["project"] = {"key": meta_issue.project_code}
    option, _ = pick(meta_issue.issue_type_names, "Issue type", indicator=INDICATOR)
    fields["issuetype"] = {"name": option}
    click.echo(f"Issue type: {option}")
    fields["summary"] = click.prompt("Summary", type=str)
    fields["description"] = click.prompt("Description", type=str)
    # Iterate if there is any other required
    for field in meta_issue.required_fields(fields["issuetype"]["name"]):
        if field["key"] not in [
            "project",
            "issuetype",
            "summary",
            "description",
            "reporter",
        ]:
            fields[field["key"]] = prompt_field(field)
    return fields


def pick_branch_format():
    try:
        options = Config().jira["branch_formats"]
    except:
        options = ["issue_key-issue_summary"]
    option, _ = pick(
        options + ["Specify custom branch format"],
        "Select a branch format name",
        indicator=INDICATOR,
    )

    if option == "Specify custom branch format":
        option = click.prompt(
            "Specify custom branch format.\nUse issue_key and issue_summary as placeholders",
            type=str,
        )

    return option


@click.command()
@click.option(
    "-k",
    "--issue-key",
    "issue_key",
    help="Create an branch using an existing issue",
    type=str,
)
@click.option(
    "-f",
    "--format",
    is_flag=True,
    show_default=False,
    default=False,
    help="Pick from the configured branch formats or specify a new one",
)
def branch(issue_key, format):
    if issue_key:
        issue = JiraIssue(issue_key=issue_key)
        msg = f"Branch created! See issue: {issue.url}"
    else:
        issue = JiraIssue(input_fields=issue_fields_input())
        msg = f"{issue.type} created at {issue.url}"
        assignee = assign_issue(issue)
        if assignee:
            msg = f"{msg}. Assgined to: {assignee}"

    if format:
        branch_format = pick_branch_format()
    else:
        try:
            branch_format = Config().jira["branch_formats"][0]
        except:
            branch_format = "issue_key-issue_summary"

    GitBranch(
        issue_key=issue.key, issue_summary=issue.summary, name_format=branch_format
    ).create()

    click.echo(msg)
