import sys
import click
from pick import pick
from git_jira.git import GitBranch
from git_jira.jira import Jira, JiraIssue
from git_jira.utils import INDICATOR


def update_status(issue):
    new_value, _ = pick(
        [status["display_name"] for status in issue.available_statuses]
        + ["Cancel status update"],
        "Update to:",
        indicator=INDICATOR,
    )
    if new_value != "Cancel status update":
        new_value_name = [
            status["name"]
            for status in issue.available_statuses
            if status["display_name"] == new_value
        ][0]
        Jira().jira.transition_issue(issue.issue, new_value_name)
    else:
        new_value = False
    return new_value


def assign_issue(issue):
    new_value, _ = pick(
        ["To me", "To another user", "Do not assign"],
        "Assign issue to:",
        indicator=INDICATOR,
    )
    j = Jira()
    if new_value == "To me":
        assignee = j.config["username"]
    elif new_value == "To another user":
        assignee = click.prompt("User email", type=str)
    else:
        assignee = False
    if assignee:
        j.jira.assign_issue(issue=issue.issue, assignee=assignee)
    return assignee


@click.command()
# All these options should be to update something. No options means show info.
@click.option(
    "-s",
    "--status",
    is_flag=True,
    show_default=False,
    default=False,
    help="Change the issue status",
)
@click.option(
    "-a",
    "--assign",
    is_flag=True,
    show_default=False,
    default=False,
    help="Change the issue assignee",
)
@click.option("-c", "--comment", help="Add a comment to the issue")
def issue(status, assign, comment):
    branch = GitBranch()
    if branch.issue_key:
        issue = JiraIssue(issue_key=branch.issue_key)
        if status:
            new_value = update_status(issue)
            if new_value:
                click.echo(f"Status of issue {issue.key} updated to {new_value}")
            else:
                click.echo(f"Status update canceled.")
        elif assign:
            new_assignee = assign_issue(issue)
            if new_assignee:
                click.echo(f"Issue {issue.key} assigned to {new_assignee}")
            else:
                click.echo(f"Issue assignation canceled.")
        elif comment:
            c = Jira().jira.add_comment(issue=issue.issue, body=comment)
            click.echo(
                f"Comment added. See it here: {issue.url}?focusedCommentId={c.id}"
            )
        else:
            click.echo(f"Issue type: {issue.type}")
            click.echo(f"Summary: {issue.summary}")
            click.echo(f"Assigned to: {issue.assignee}")
            click.echo(f"Status: {issue.status}")
            click.echo(f"See more at {issue.url}")
    else:
        click.echo("No issue found for this branch.")
