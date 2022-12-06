import typer

import isolate_cloud.auth as auth

cli = typer.Typer()

@cli.command()
def login(revoke: bool = False):
    if revoke:
        auth.logout()
    else:
        auth.login()

@cli.command(hidden=True)
def hello():
    """
    To test auth.
    """
    print(f"Hello, {auth.USER.info['name']}")

if __name__ == "__main__":
    cli()
