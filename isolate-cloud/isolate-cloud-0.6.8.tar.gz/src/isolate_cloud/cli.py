from __future__ import annotations

import isolate_cloud.auth as auth
import isolate_cloud.sdk as sdk
import typer

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


key_cli = typer.Typer()


@key_cli.command(name="generate")
def generate_key(host: str = "localhost", port: str = "6005"):
    connection = sdk.FalHostedGrpcConnection(f"{host}:{port}")
    result = connection.create_user_key()
    print(
        "Generated key id and key secret.\n"
        "This is the only time the secret will be visible.\n"
        "You will need to generate a new key pair if you lose access to this secret."
    )
    print(f"KEY_ID='{result.key_id}'\nKEY_SECRET='{result.key}'")


cli.add_typer(key_cli, name="key")

if __name__ == "__main__":
    cli()
