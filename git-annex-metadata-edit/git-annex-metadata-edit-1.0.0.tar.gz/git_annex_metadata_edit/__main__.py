# system modules
import argparse
import itertools
import json
import logging
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile

# internal modules
from git_annex_metadata_edit.version import __version__

logger = logging.getLogger("git-annex-metadata-edit")


def git_annex_fieldname(s):
    if not re.fullmatch(r"[a-z0-9_.-]+", s, flags=re.IGNORECASE):
        raise argparse.ArgumentTypeError(
            f"Given fieldname {s!r} is not allowed"
            " (only alphanumerics and _-.)"
        )
    return s


parser = argparse.ArgumentParser(
    description=f"Edit git-annex metadata with you $EDITOR"
    f"\n\nversion {__version__}"
)
parser.add_argument("field", type=git_annex_fieldname, help="Tag to edit")
parser.add_argument(
    "files",
    metavar="file",
    nargs="*",
    default=["."],
    help="Files to edit the metadata for",
)
parser.add_argument(
    "--noconfirm",
    action="store_true",
    help="Don't ask before executing modifying git-annex commands",
)
parser.add_argument(
    "-v", "--verbose", action="store_true", help="No debug output"
)


def nonempty(x):
    return filter(bool, x)


def vipe(inputstr: str, suffix=".md") -> str:
    if not (
        editor := next(
            nonempty(
                shutil.which(editor)
                for editor in (
                    [
                        os.environ.get(envvar, "")
                        for envvar in ("VISUAL", "EDITOR")
                    ]
                    + ["nano", "pico", "vim", "vi"]
                )
            ),
            None,
        )
    ):
        raise FileNotFoundError(
            "🤷 No Editor found. Set VISUAL or EDITOR environment variable."
        )
    try:
        _, tmpfile = tempfile.mkstemp(
            prefix="git-annex-metadata-edit-", suffix=suffix
        )
        with open(tmpfile, "w") as fh:
            fh.write(inputstr)
        subprocess.run([editor, tmpfile])
        with open(tmpfile, "r") as fh:
            outputstr = fh.read()
    finally:
        try:
            os.remove(tmpfile)
        except (NameError, OSError) as error:
            logger.error(f"⚠️  Couldn't remove {tmpfile = !r}: {error = !r}")
    return outputstr.removesuffix("\r\n").removesuffix("\n")


def cli():
    args = parser.parse_args()
    if os.path.exists(args.field) or os.path.islink(args.field):
        parser.error(
            f"⚠️  It looks like your field {args.field!r} is an existing file. "
            f"Specify a field as *first* argument "
            "and the files as following arguments!"
        )
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.WARNING
    )
    logger.debug(f"{args = }")

    def run(cmdline):
        logger.debug(f"{cmdline = }")
        if not args.noconfirm:
            input(f"Run {cmdline}? [Hit ENTER ↩️ ]")
        logger.debug(f"Running {shlex.join(cmdline)!r}...")
        subprocess.run(cmdline)

    try:
        git_annex_metadata_jsonlines = subprocess.check_output(
            ["git", "annex", "metadata", "--json"] + args.files,
            encoding="utf-8",
            errors="ignore",
        )
    except subprocess.CalledProcessError as e:
        logger.error(f"💥 {e}")
        sys.exit(1)
    # logger.debug(f"{git_annex_metadata_jsonlines = }")
    old_metadata = {}
    for line in git_annex_metadata_jsonlines.splitlines():
        m = json.loads(line)
        logger.debug(f"{m['input'] = },  {m['fields'] = }")
        for path in m.get("input", tuple()):
            if value := m.get("fields", {}).get(args.field, tuple()):
                old_metadata[path] = value
    logger.debug(f"{old_metadata = }")
    if all(
        len(list(nonempty(v.splitlines()))) == 1
        for v in itertools.chain.from_iterable(old_metadata.values())
    ):
        values = sorted(
            set(itertools.chain.from_iterable(old_metadata.values()))
        )
        merged_metadata = "\n".join(
            (f"+ {v}" for v in values) if len(values) > 1 else values
        )
    else:
        merged_metadata = "\n\n".join(
            nonempty(
                set(
                    (v if isinstance(v, str) else "\n".join(v))
                    for k, v in sorted(old_metadata.items())
                )
            )
        )
    logger.debug(f"{merged_metadata = }")
    comment = f"""
-------------------------------------------------------------------------------
⬆⬆⬆ ✍️  Write the new content of the {args.field!r}-field ABOVE this line ⬆⬆⬆
               🚫 ! DON'T REMOVE OR EDIT THAT LINE OF DASHES! 🚫

If you specify a list of single-line values like this:

- value1-to-remove
+ value2-to-add
+ value3-to-add
- value4-to-remove

... then the {args.field!r}-field will be adjusted accordingly for all files (- means remove the value from {args.field!r}, + means add this value from {args.field!r})

Otherwise, the {args.field!r}-field will be overwritten with the single value specified here.

Empty input will cause the {args.field!r} to be removed.

✂️  Leading and trailing whitespace will be stripped.

The following files will have the {args.field!r}-field set:

{chr(10).join('📁  '+f for f in args.files)}
"""
    editor_content = f"{merged_metadata}\n{comment}"
    while True:  # open user's EDITOR until they made a proper edit
        editor_result = vipe(editor_content, suffix=f"-{args.field}.md")
        logger.debug(f"{editor_result = }")
        if m := re.search(
            r"^\s*-{10,}\s*$", editor_result, flags=re.MULTILINE
        ):
            new_value = editor_result[: m.span()[0]].strip()
            break
        else:
            logger.error("Please don't edit the trailing comment.")
            if sys.stdin.isatty():
                input("Editor will reopen now [Press ENTER ↩️ ]")
            else:
                print(
                    f"Here is the editor's content in case you want to copy it:"
                    f"\n{editor_result}"
                )
                sys.exit(1)
            # start over with the comment appended again
            editor_content = f"{editor_result}\n{comment}"
            continue
        break
    logger.debug(f"{new_value = !r}")
    if not new_value:
        run(
            [
                "git",
                "annex",
                "metadata",
                "--force",
                "--remove",
                args.field,
            ]
            + list(args.files)
        )
    elif all(
        addremovelines := [
            next(iter(re.findall(r"^\s*([+-])\s*(.+?)\s*$", L)), [])
            for L in nonempty(new_value.splitlines())
        ]
    ):
        logger.debug(f"{addremovelines = }")
        for action in "-+":
            for value in set(v for a, v in addremovelines if action in a):
                run(
                    [
                        "git",
                        "annex",
                        "metadata",
                        "--force",
                        "--set",
                        f"{args.field}{action}={value.strip()}",
                    ]
                    + list(args.files)
                )
    else:
        new_metadata = {f: [new_value] for f in args.files}
        logger.debug(f"{new_metadata = }")
        run(
            [
                "git",
                "annex",
                "metadata",
                "--force",
                "--set",
                f"{args.field}={new_value.strip()}",
            ]
            + list(args.files)
        )


if __name__ == "__main__":
    cli()
