import plistlib
import re
import tempfile
from collections import deque

import click
import inflect as ifl
import pygit2
import validators
from InquirerPy.base import Choice
from github import Github as GitHub
from github.GithubException import UnknownObjectException
from halo import Halo
from path import Path
from prompt_toolkit.document import Document
from prompt_toolkit.validation import Validator, ValidationError

import helpers
import prompts

inflect = ifl.engine()


def add_from_builtins():
    add(helpers.get_builtin_schemes_dir())


def add_from_github():
    gh = GitHub()
    repo_regex = re.compile(r"^(?P<owner>[^/]+)/(?P<repo>[^/]+)$")

    def repo_name_processor(result: str) -> str:
        url_regex = re.compile(r"(?<=github.com/)[a-zA-Z0-9-_.]+/[a-zA-Z0-9-_.]+")
        match = url_regex.search(result, re.IGNORECASE)
        if match:
            return match.group(0)
        else:
            return result

    while True:
        token = None

        repo_name = prompts.text(
            message="Enter the name or URL of a GitHub repository.",
            instruction="e.g. celsiusnarhwal/beenine",
            validate=lambda result: validators.url(result) or repo_regex.match(result),
            filter=repo_name_processor,
            invalid_message="Invalid GitHub repository.",
        ).execute()

        try:
            repo = gh.get_repo(repo_name)
        except UnknownObjectException:
            msg = f"{repo_name} may be private. You'll need to sign in to GitHub."
            click.echo(helpers.make_info_text(msg))

            token = helpers.sign_in_to_github()

            if token is None:
                continue
            elif token is False:
                click.echo(helpers.make_error_text("Schemarin was denied access to your GitHub account."))
                continue
            else:
                gh = GitHub(token)
                try:
                    repo = gh.get_repo(repo_name)
                except UnknownObjectException:
                    msg = f"{repo_name} either doesn't exist or isn't accessible to your GitHub account."
                    click.echo(helpers.make_error_text(msg))
                    continue

        tmpdir = tempfile.mkdtemp()

        with Halo(text="Loading repository contents...", spinner="dots") as spinner:
            try:
                callbacks = pygit2.RemoteCallbacks(pygit2.UserPass(token, "x-oauth-basic"))
                pygit2.clone_repository(repo.clone_url, tmpdir, callbacks=callbacks)
            except pygit2.GitError:
                try:
                    callbacks = pygit2.RemoteCallbacks(pygit2.UserPass(gh.get_user().login, token))
                    pygit2.clone_repository(repo.clone_url, tmpdir, callbacks=callbacks)
                except pygit2.GitError:
                    isnt = click.style("isn't", underline=True)  # because f-strings can't have backslashes, lol
                    spinner.fail(f"There was an error cloning {repo.full_name}. This {isnt} your fault. "
                                 f"Try again later.")
                    continue
                else:
                    spinner.succeed("Repository loaded!")
                    add(Path(tmpdir))
                    break
            else:
                spinner.succeed("Repository loaded!")
                add(Path(tmpdir))
                break


def add_from_files():
    class FilepathValidator(Validator):
        def validate(self, document: Document) -> None:
            if not Path(document.text).exists():
                raise ValidationError(message="That path doesn't exist.")
            if Path(document.text).isfile() and Path(document.text).ext != ".itermcolors":
                raise ValidationError(message="That's not an iTermColors file.")

    path: Path = prompts.filepath(
        message="Enter the path to a iTermColors file or a directory containing some.",
        instruction="Relative paths and symbolic links are fully supported.",
        long_instruction=f"The current working directory is {Path.getcwd().realpath()}.",
        validate=FilepathValidator(),
        filter=lambda result: Path(result).expand().realpath(),
        transformer=lambda result: Path(result).expand().realpath(),
    ).execute()

    if path.isfile():
        with tempfile.TemporaryDirectory() as tmpdir:
            td_path = Path(tmpdir)
            path.copy(td_path)
            add(td_path)
    else:
        add(path)


def add(path: Path):
    with Halo(text="Looking for color schemes...", spinner="dots") as spinner:
        try:
            colorfiles = {p.realpath(): plistlib.load(p.open("rb")) for p in path.walk("*.itermcolors")}
        except PermissionError as e:
            helpers.resolve_permission_error(path, e, spinner)
            raise KeyboardInterrupt
        else:
            existing = helpers.get_scheme_settings()
            deque(maxlen=0).extend(
                colorfiles.pop(p.realpath(), None)
                for key in existing.keys() for p in path.walk(f"{key}.itermcolors")
            )

        if not colorfiles:
            if path == helpers.get_builtin_schemes_dir():
                spinner.fail("You've already added all the built-in color schemes. Impressive!")
            else:
                spinner.fail("There are no color schemes there that you don't already have.")
            raise KeyboardInterrupt
        elif len(colorfiles) == 1:
            schemes = [colorfiles][0]
            spinner.info("There's only one color scheme here that you don't already have, so Schemarin will go ahead "
                         "and add it.")
        else:
            spinner.succeed("Color schemes loaded!")
            schemes = prompts.fuzzy(
                message="Choose some color schemes.",
                instruction="Type to search. Color schemes you already have are not listed.",
                long_instruction=helpers.MULTISELECT_CONTROLS,
                choices=sorted(
                    [Choice(name=path.stem, value=path) for path in colorfiles],
                    key=lambda choice: choice.name),
                multiselect=True,
                transformer=lambda result: f"Adding {inflect.no('color scheme', len(result))}.",
            ).execute()

    scheme_settings = helpers.get_scheme_settings()

    for scheme in schemes:
        scheme_settings[scheme.stem] = plistlib.load(scheme.open("rb"))

    helpers.save_scheme_settings(scheme_settings)

    msg = f"Added {helpers.get_scheme_indicator(schemes)}. Restart iTerm2 to apply your changes."
    click.echo(helpers.make_success_text(msg))

    if path.realpath().startswith(Path(tempfile.gettempdir()).realpath()):
        path.rmtree()
