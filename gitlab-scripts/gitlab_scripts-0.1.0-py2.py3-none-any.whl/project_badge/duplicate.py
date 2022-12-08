import argparse
import sys

from imxdparser import SubParser

from ..gitlab import connect


def main(parent_parser):
    project_badge_duplicate = SubParser(
        parent_parser,
        "duplicate",
    )
    parser = project_badge_duplicate.parser
    parser.add_argument("src", help="Lorem ipsum sit dolor amet")
    parser.add_argument("dst", help="Lorem ipsum sit dolor amet")

    parser.add_argument(
        "--delete",
        default=True,
        help="Lorem ipsum sit dolor amet",
        action="store_true",
        dest="delete",
    )
    parser.add_argument(
        "--no-delete",
        default=False,
        help=argparse.SUPPRESS,
        action="store_false",
        dest="delete",
    )
    parser.add_argument(
        "--replace",
        default=True,
        help="Lorem ipsum sit dolor amet",
        action="store_true",
        dest="replace",
    )
    parser.add_argument(
        "--no-replace",
        default=False,
        help=argparse.SUPPRESS,
        action="store_false",
        dest="replace",
    )
    project_badge_duplicate.set_defaults(func=action)


def action(cfg, args):
    gitlab = connect(cfg)
    src = args["src"]
    dst = args["dst"]

    src_prj = gitlab.projects.get(src)
    dst_prj = gitlab.projects.get(dst)

    if args["delete"]:
        print(f'Deleting project badges from "{dst_prj.web_url}"...', file=sys.stderr)
        for badge in dst_prj.badges.list(iterator=True):
            dst_prj.badges.delete(id=badge.id)

    print(f'Copying project badges from "{src_prj.web_url}" to "{dst_prj.web_url}"...', file=sys.stderr)
    for badge in src_prj.badges.list(iterator=True):
        desc = badge.asdict()

        if args["replace"]:
            for url in ["image_url", "link_url"]:
                desc[url] = desc[url].replace(src_prj.path, dst_prj.path)
        dst_prj.badges.create(badge.asdict())
    print(f'Copied project badges from "{src_prj.web_url}" to "{dst_prj.web_url}".', file=sys.stderr)
