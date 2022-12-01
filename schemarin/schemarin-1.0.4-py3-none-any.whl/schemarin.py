import json
import plistlib
import re
import subprocess
import sys
import zipfile
from datetime import datetime

import click
import inflect as ifl
from InquirerPy.base import Choice
from colour import Color
from path import Path
from prompt_toolkit.document import Document
from prompt_toolkit.validation import Validator, ValidationError

import helpers
import importers
import prompts


inflect = ifl.engine()


def add_schemes():
    source = prompts.select(
        message="Where from?",
        choices=[
            Choice(name="Built-in color schemes", value="builtin"),
            Choice(name="GitHub repository", value="github"),
            Choice(name="Local files", value="local"),
        ]
    ).execute()

    if source == "builtin":
        importers.add_from_builtins()
    elif source == "github":
        importers.add_from_github()
    elif source == "local":
        importers.add_from_files()


def remove_schemes():
    scheme_settings = helpers.get_scheme_settings()

    scheme_choices = [name for name in scheme_settings.keys()]

    if not scheme_choices:
        click.echo(helpers.make_error_text("You haven't added any color schemes."))
        raise KeyboardInterrupt

    if len(scheme_choices) == 1:
        schemes = [scheme_choices[0]]
        click.echo(helpers.make_info_text("You only have one removable color scheme."))
    else:
        scheme_choices.sort(key=lambda c: c.lower())

        schemes = prompts.fuzzy(
            message="Choose color schemes to remove.",
            instruction="Type to search.",
            long_instruction=helpers.MULTISELECT_CONTROLS,
            choices=scheme_choices,
            multiselect=True,
            transformer=lambda result: f"Removing {inflect.no('color scheme', len(result))}.",
        ).execute()

    if len(schemes) <= 5:
        scheme_indicator = inflect.join([scheme for scheme in schemes])
    else:
        scheme_indicator = inflect.no('color scheme', len(schemes))

    if prompts.confirm(f"Remove {scheme_indicator}?").execute():
        for scheme in schemes:
            del scheme_settings[scheme]

        helpers.save_scheme_settings(scheme_settings)

        click.echo(helpers.make_success_text(f"Removed {scheme_indicator}. Restart iTerm2 to apply your changes."))


def export_schemes():
    scheme_settings = helpers.get_scheme_settings()

    scheme_choices: list[str] = [name for name in scheme_settings.keys()]

    if not scheme_choices:
        click.echo(helpers.make_error_text("You haven't added any color schemes."))
        raise KeyboardInterrupt

    if len(scheme_choices) == 1:
        schemes = [scheme_choices[0]]
        click.echo(helpers.make_info_text(f"You only have one exportable color scheme. ({scheme_choices[0]})"))
    else:
        scheme_choices.sort(key=lambda c: c.lower())

        schemes: list[str] = prompts.fuzzy(
            message="Choose color schemes to export.",
            instruction="Type to search.",
            long_instruction=helpers.MULTISELECT_CONTROLS,
            choices=scheme_choices,
            multiselect=True,
            transformer=lambda result: f"Exporting {inflect.no('color scheme', len(result))}.",
        ).execute()

    format_choices = [
        Choice(name="iTermColors", value="itermcolors"),
        Choice(name="JSON", value="json"),
        Choice(name="XML", value="xml"),
        Choice(name="Property list", value="plist"),
    ]

    export_format: str = prompts.select(
        message="Choose an export format.",
        instruction="Only iTermColors files can be imported back into iTerm2.",
        choices=format_choices,
    ).execute()

    export_dir: Path = prompts.filepath(
        message="Choose a directory to export to.",
        instruction="Relative paths and symbolic links are fully supported.",
        long_instruction=f"The current working directory is {Path.getcwd()}.",
        validate=lambda result: Path(result).expand().isdir(),
        invalid_message="That's not a directory.",
        filter=lambda result: Path(result).expand().realpath(),
        transformer=lambda result: Path(result).expand().realpath(),
    ).execute()

    if len(schemes) <= 5:
        scheme_indicator = inflect.join([scheme for scheme in schemes])
    else:
        scheme_indicator = inflect.no("color scheme", len(schemes))

    date = datetime.today().strftime('%x').replace('/', '-')
    if len(schemes) == 1:
        scheme = schemes[0]
        export_path = export_dir / f"{scheme}.{export_format}"

        if export_path.exists():
            if not prompts.confirm(f"{export_path} already exists. Overwrite it?").execute():
                raise KeyboardInterrupt

        if export_format == "json":
            json.dump(scheme_settings[scheme], export_path.open("w"))
        else:
            plist_format = plistlib.FMT_BINARY if export_format == "plist" else plistlib.FMT_XML
            plistlib.dump(scheme_settings[scheme], export_path.open("wb"), fmt=plist_format)
    else:
        export_path = export_dir / f"schemarin_{export_format}_export_{date}.zip"

        if export_path.exists():
            if not prompts.confirm(f"{export_path} already exists. Overwrite it?").execute():
                raise KeyboardInterrupt

        with zipfile.ZipFile(export_dir / f"schemarin_{export_format}_export_{date}.zip", mode="w") as archive:
            for scheme in schemes:
                export_name = f"{scheme}.{export_format}"
                if export_format == "json":
                    archive.writestr(export_name, json.dumps(scheme_settings[scheme]))
                else:
                    plist_format = plistlib.FMT_BINARY if export_format == "plist" else plistlib.FMT_XML
                    archive.writestr(export_name, plistlib.dumps(scheme_settings[scheme], fmt=plist_format))

    click.echo(helpers.make_success_text(f"Exported {scheme_indicator} to {export_path}."))


def preview_schemes():
    class PreviewValidator(Validator):
        def validate(self, document: Document) -> None:
            preview_scheme = scheme_settings[document.text]
            for k, v in preview_scheme.items():
                click.echo(get_ansi_code(k, v), nl=False)

            raise ValidationError(message=f"Previewing {document.text}.")

    def get_ansi_code(attr_name: str, attr_data: dict) -> str:
        if re.match(r"Ansi \d+ Color", attr_name):
            ansi_id = int(re.search(r"\d+", attr_name).group())
            attr_code = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
                         "br_black", "br_red", "br_green", "br_yellow", "br_blue", "br_magenta",
                         "br_cyan", "br_white"][ansi_id]
        else:
            attr_code = {
                "Foreground Color": "fg",
                "Background Color": "bg",
                "Bold Color": "bold",
                "Selection Color": "selbg",
                "Selected Text Color": "selfg",
                "Cursor Color": "curbg",
                "Cursor Text Color": "curfg",
            }.get(attr_name, "")

        red = attr_data["Red Component"]
        green = attr_data["Green Component"]
        blue = attr_data["Blue Component"]
        color_hex = Color(rgb=(red, green, blue)).hex.lstrip("#")

        return f"\033]1337;SetColors={attr_code}={color_hex}\033\\"

    if not Path("~/.iterm2/it2check").expand().exists():
        msg = "Please install iTerm2's shell integration."
        info_msg = "Learn more: https://iterm2.com/documentation-shell-integration.html"
        click.echo(helpers.make_error_text(msg))
        click.echo(helpers.make_info_text(info_msg))
        raise KeyboardInterrupt

    if not subprocess.run("~/.iterm2/it2check", stdout=sys.stdout, shell=True).returncode == 0:
        msg = "Please quit Schemarin and relaunch it from within iTerm2."
        click.echo(helpers.make_error_text(msg))
        raise KeyboardInterrupt

    scheme_settings = helpers.get_scheme_settings()

    scheme_choices: list[str] = [name for name in scheme_settings.keys()]

    if not scheme_choices:
        click.echo(helpers.make_error_text("You haven't added any color schemes."))
        raise KeyboardInterrupt

    scheme_choices.sort(key=lambda c: c.lower())

    try:
        prompts.fuzzy(
            message="Choose a color scheme to preview.",
            instruction="Type to search.",
            long_instruction="Preview colors may not be perfectly accurate.",
            choices=scheme_choices,
            validate=PreviewValidator(),
        ).execute()
    except KeyboardInterrupt:
        msg = "To return to your original color scheme, open a new terminal tab or window."
        click.echo(helpers.make_info_text(msg))
        raise KeyboardInterrupt


def main():
    print("Schemarin © 2022-present celsius narhwal. Licensed under MIT (see --license).\n")

    while True:
        try:
            prompts.select(
                message="What would you like to do?",
                choices=[Choice(name="Add color schemes", value=add_schemes),
                         Choice(name="Remove color schemes", value=remove_schemes),
                         Choice(name="Export color schemes", value=export_schemes),
                         Choice(name="Preview color schemes", value=preview_schemes),
                         Choice(name="Quit Schemarin", value=exit)],
                transformer=lambda result: "Goodbye!" if "quit" in result.casefold() else result
            ).execute()()
        except KeyboardInterrupt:
            # Aside from effectively binding Control + C to the main menu, this allows Schemarin to easily
            # force returns to the main menu by explicitly raising KeyboardInterrupt exceptions.
            click.echo(helpers.make_info_text("Returning to the main menu."))
            continue


@click.command()
@click.option("--license", "show_license", is_flag=True, help="See schemarin's license.")
def cli(show_license):
    if not helpers.preflight():
        exit(1)
    elif show_license:
        click.echo((Path(__file__).parent / "LICENSE.md").read_text())
    else:
        main()


if __name__ == "__main__":
    cli()
