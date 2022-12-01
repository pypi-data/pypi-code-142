import platform
import plistlib
import sys
import time

import click
import inflect as ifl
import pyperclip
import toml
from InquirerPy.base import Choice
from github import Github as GitHub
from github.GithubException import BadCredentialsException
from halo import Halo
from loctocat import GitHubAuthenticator
from loctocat import Handler
from loctocat import ServerError
from path import Path
from prompt_toolkit.document import Document
from prompt_toolkit.validation import Validator, ValidationError

import prompts

inflect = ifl.engine()

IT2_PREFS_PATH = Path("~/Library/Preferences/com.googlecode.iterm2.plist").expand()

MULTISELECT_CONTROLS = ("↑/↓: Move up and down\n"
                        "Control + Z: Toggle selection\n"
                        "Control + A: Toggle all on/off\n"
                        "Enter: Confirm\n")


def preflight():
    passing = True

    if sys.platform != "darwin":
        click.echo(make_error_text("Schemarin only works on macOS. Sorry!"))
        passing = False
    elif not IT2_PREFS_PATH.exists():
        click.echo(make_error_text("schemarin couldn't find iTerm2's preferences file. "
                                   "Install iTerm2 from https://iterm2.com. If iTerm2 is installed and you're still "
                                   "seeing this message, file an issue on GitHub: "
                                   "https://github.com/celsiusnarhwal/schemarin/issues"))
        passing = False

    return passing


def get_scheme_indicator(schemes: list) -> str:
    if len(schemes) <= 5:
        return inflect.join([scheme.stem for scheme in schemes])
    else:
        return inflect.no("color scheme", len(schemes))


def get_it2_prefs():
    return plistlib.load(IT2_PREFS_PATH.open("rb"))


def get_scheme_settings():
    return get_it2_prefs()["Custom Color Presets"]


def save_scheme_settings(settings: dict):
    prefs = get_it2_prefs()
    prefs["Custom Color Presets"] = settings
    plistlib.dump(prefs, IT2_PREFS_PATH.open("wb"))


def get_builtin_schemes_dir():
    return Path(__file__).parent / "schemes" / "schemes"


def make_info_text(text: str):
    return f"{click.style('ℹ', fg='blue')} {text}"


def make_success_text(text: str):
    return f"{click.style('✔', fg='green')} {text}"


def make_error_text(text: str):
    return f"{click.style('✖', fg='red')} {text}"


def sign_in_to_github():
    token = None

    class AuthMenuValidator(Validator):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.last_poll_time = None

        def validate(self, document: Document) -> None:
            if document.text == "done":
                if self.last_poll_time and time.time() - self.last_poll_time < 5:
                    raise ValidationError(message="Slow your roll. Try again in a few seconds.")
                else:
                    nonlocal token
                    try:
                        token = authenticator.poll()
                    except ServerError:
                        token = False
                    else:
                        if not token:
                            self.last_poll_time = time.time()
                            raise ValidationError(message="No you didn't.")
            elif document.text == "copy":
                pyperclip.copy(auth_info.user_code)
                raise ValidationError(message="Code copied to clipboard.")
            elif document.text == "open":
                click.launch(auth_info.verification_uri)
                raise ValidationError(message="Browser opened.")

    authenticator = GitHubAuthenticator(client_id="05cf23375abbfca11121", scopes=["repo"])
    authenticator.attach_handler(Handler("authorization_pending", lambda ctx: None, continue_on_error=False))

    auth_info = authenticator.ping()

    auth_menu_choices = [
        Choice(name="I did it", value="done"),
        Choice(name="Copy code to clipboard", value="copy"),
        Choice(name="Open URL in browser", value="open"),
        Choice(name="I'd rather log in with a token", value="token"),
        Choice(name="Go back", value="redo"),
    ]

    auth_menu_result = prompts.select(
        message=f"Go to {auth_info.verification_uri}, enter the code {auth_info.user_code}, and click "
                f"\"Authorize\".",
        choices=auth_menu_choices,
        validate=AuthMenuValidator(),
        transformer=lambda result: f"Signed in as {GitHub(token).get_user().login}" if token else result
    ).execute()

    if auth_menu_result == "token":
        return sign_in_to_github_with_token()
    elif auth_menu_result == "redo":
        return None
    elif auth_menu_result == "done":
        return token


def sign_in_to_github_with_token():
    class TokenValidator(Validator):
        def validate(self, document: Document) -> None:
            try:
                # noinspection PyStatementEffect
                GitHub(document.text).get_user().login
            except BadCredentialsException:
                raise ValidationError(message="Invalid token.")

    token = prompts.secret(
        message="Enter a personal access token with appropriate permissions.",
        long_instruction="Need help? https://token.schemarin.celsiusnarhwal.dev",
        validate=TokenValidator(),
        transformer=lambda result: f"Signed in as {GitHub(result).get_user().login}"
    ).execute()

    return token


def resolve_permission_error(path: Path, exception: PermissionError, spinner: Halo):
    failed_path = Path(exception.filename)
    protected = [Path(x) for x in
                 (["/System", "/usr", "/bin", "/sbin", "/var"] +
                  [*toml.load(Path(__file__).parent / "protected.toml")["apps"].values()])]

    if any(failed_path.realpath().startswith(p.realpath()) for p in protected):
        if failed_path == path:
            msg = f"{path} is protected by macOS. "
        else:
            msg = f"{failed_path}, a subdirectory of {path}, is protected by macOS. "
        msg += (f"To allow Schemarin access to it, you must disable System Integrity Protection "
                f"{click.style('(very bad idea)', fg='red', bold=TabError)} and rerun Schemarin with sudo.")

        spinner.fail(msg)

        info = "Learn more: https://schemarin.celsiusnarhwal.dev/blob/HEAD/schemarin-and-sip.md"
        click.echo(make_info_text(info))
    else:
        macos_version = platform.mac_ver()[0].split(".")
        macos_version = ".".join(macos_version[:2])
        if failed_path == path:
            msg = f"You don't have permissions to access {path}. "
        else:
            msg = f"You don't have permission to access {failed_path}, which is a subdirectory of {path}. "

        msg += "Try running Schemarin with sudo."
        spinner.fail(msg)

        click.echo(make_info_text(f"Learn more: https://support.apple.com/guide/mac-help/"
                                  f"change-permissions-for-files-folders-or-disks-mchlp1203/{macos_version}"))
