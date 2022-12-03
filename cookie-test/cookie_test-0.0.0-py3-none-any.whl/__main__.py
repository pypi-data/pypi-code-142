"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Cookie Test."""


if __name__ == "__main__":
    main(prog_name="cookie-test")  # pragma: no cover
