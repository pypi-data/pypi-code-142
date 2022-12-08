import random
import sys
from collections import Counter
from datetime import date, datetime
from functools import wraps
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

import yapx
from watchfiles import Change, watch

from .__version__ import __version__
from .exceptions import SiteNameRequiredError, UnrecognizedStatusUpdateError
from .models import ComparisonResult, PubliiPostComparison, StatusUpdate, ValidFilters
from .siinc import Siinc
from .utils import millis_to_date, millis_to_datetime, tabulate_dict

SIINC_KWARGS: Dict[str, Any] = {}


def setup(
    site_home: Optional[Path] = yapx.arg(
        None, env="PUBLII_SITE_HOME", flags=["--site-home"]
    ),
    site_name: Optional[Path] = yapx.arg(
        None, env="PUBLII_SITE_NAME", flags=["-d", "--site"]
    ),
    db_name: Path = yapx.arg(Path("db.sqlite"), env="PUBLII_DB", flags=["--db"]),
    posts_home: Path = yapx.arg(
        Path("posts"), env="PUBLII_POSTS_HOME", flags=["--posts"]
    ),
    posts_path_format: Optional[str] = yapx.arg(
        r"{status}/{tag}/{author}/{date}",
        env="PUBLII_PATH_FORMAT",
        flags=["--path-format"],
    ),
    posts_date_format: Optional[str] = yapx.arg(
        None, env="PUBLII_DATE_FORMAT", flags=["--date-format"]
    ),
    privileged: bool = yapx.arg(
        False, flags=["-p", "--privileged"], env="PUBLII_SIINC_PRIVILEGED"
    ),
    delete_orphans: bool = yapx.arg(
        False, flags=["-x", "--delete-orphans"], env="PUBLII_SIINC_DELETE_ORPHANS"
    ),
    version: bool = yapx.arg(False, group="version", flags=["--version"]),
) -> None:
    if version:
        print(__version__)
        sys.exit(0)

    if posts_path_format and posts_path_format.lower() == "none":
        posts_path_format = None
    if posts_date_format and posts_date_format.lower() == "none":
        posts_date_format = None

    if site_home or site_name:
        if site_home:
            if not site_home.exists():
                raise FileNotFoundError(site_home)
            if not site_name:
                raise SiteNameRequiredError(
                    f"Site name missing. Specify one of: {list(site_home.glob('*'))}"
                )
        elif site_name:
            if not site_name.exists():
                raise FileNotFoundError(site_name)
            site_home = site_name.parent
            site_name = Path(site_name.name)

        assert site_home
        assert site_name
        site_path: Path = site_home / site_name

        db_name = site_path / "input" / db_name
        posts_home = site_path / posts_home

        if site_path.exists():
            posts_home.mkdir(exist_ok=True)
    else:
        if not db_name:
            raise ValueError("Missing value for `--db`")
        if not posts_home:
            raise ValueError("Missing value for `--posts`")
        posts_home.mkdir(exist_ok=True)

    SIINC_KWARGS.update(
        {
            "db": db_name,
            "directory": posts_home,
            "path_format": posts_path_format,
            "path_date_format": posts_date_format,
            "privileged": privileged,
            "delete_orphans": delete_orphans,
        }
    )


def _make_data_table(
    results: List[PubliiPostComparison], include_equal: bool, verbose: bool = False
) -> List[Dict[str, Any]]:
    data_table: List[Dict[str, Any]] = [
        {
            "TAG": x.main_tag,
            "SLUG": x.slug,
            "FILE": (x.file_path if x.file_path else x.file_path_expected).relative_to(
                SIINC_KWARGS["directory"]
            ),
            "STATUS": x.status,
            "DATE_MODIFIED": millis_to_datetime(x.modified_at),
            "DATE_DIFF": millis_to_datetime(x.file_modified_at)
            - millis_to_datetime(x.modified_at)
            if x.file_modified_at
            else None,
            "CHARS": len(x.text),
            "CHARS_DIFF": len(x.file_text) - len(x.text) if x.file_text else 0,
            "WORDS": len(x.text.split()),
            "WORDS_DIFF": len(x.file_text.split()) - len(x.text.split())
            if x.file_text
            else 0,
            "RESULT": x.result.name,
        }
        for x in results
        if x.result and (include_equal or x.result != ComparisonResult.equal)
    ]
    if not verbose:
        keep_cols: List[str] = ["TAG", "SLUG", "FILE", "STATUS", "TIME_DIFF", "RESULT"]
        data_table = [
            {k: v for k, v in x.items() if k in keep_cols} for x in data_table
        ]

    return data_table


def _print_data_table(data_table: List[Dict[str, Any]]) -> None:
    if data_table:
        print(tabulate_dict(data_table))
    else:
        print("All equal; nothing to do.")


def _get_valid_filters(filters: Optional[Dict[str, str]]) -> ValidFilters:
    return ValidFilters(**(filters if filters else {}))


@wraps(_make_data_table)
def _sync(
    filters: Optional[Dict[str, str]] = None,
    force_push: bool = False,
    force_pull: bool = False,
    dry_run: bool = False,
) -> List[PubliiPostComparison]:
    with Siinc(
        filters=_get_valid_filters(filters),
        force_pull=force_pull,
        force_push=force_push,
        **SIINC_KWARGS,
    ) as client:
        results: List[PubliiPostComparison] = client.sync(dry_run=dry_run)

    return results


def sync(
    filters: Optional[Dict[str, str]] = yapx.arg(
        None, flags=["-f", "--filters"], env="PUBLII_SIINC_FILTERS"
    ),
    force_push: bool = yapx.arg(False, flags=["--force-push"], exclusive=True),
    force_pull: bool = yapx.arg(False, flags=["--force-pull"], exclusive=True),
    dry_run: bool = yapx.arg(False, flags=["--dry-run"]),
    verbose: bool = yapx.arg(False),
) -> List[PubliiPostComparison]:
    results: List[PubliiPostComparison] = _sync(
        filters=filters,
        force_push=force_push,
        force_pull=force_pull,
        dry_run=dry_run,
    )
    _print_data_table(
        _make_data_table(results=results, include_equal=False, verbose=verbose)
    )

    return results


@wraps(sync)
def list_posts(*args, _diff: bool = False, **kwargs) -> List[PubliiPostComparison]:
    verbose: bool = kwargs.pop("verbose", False)
    kwargs["dry_run"] = True
    results: List[PubliiPostComparison] = _sync(*args, **kwargs)

    _print_data_table(
        _make_data_table(results, include_equal=(not _diff), verbose=verbose)
    )

    return results


@wraps(list_posts)
def list_posts_diffs(*args, **kwargs) -> List[PubliiPostComparison]:
    kwargs["_diff"] = True
    return list_posts(*args, **kwargs)


def set_post_properties(
    filters: Optional[Dict[str, str]] = yapx.arg(
        None, flags=["-f", "--filters"], env="PUBLII_SIINC_FILTERS"
    ),
    status: Optional[StatusUpdate] = yapx.arg(None, flags="--status"),
    date_published: Optional[date] = yapx.arg(None, flags="--date-published"),
    date_modified: Optional[date] = yapx.arg(None, flags="--date-modified"),
    template: Optional[str] = yapx.arg(None, flags="--template"),
    floor_date_published: bool = yapx.arg(False, flags=["--floor-date-published"]),
    dry_run: bool = yapx.arg(False, flags=["--dry-run"]),
) -> List[PubliiPostComparison]:

    if template and template.lower() in ("global", "default"):
        template = "*"

    with Siinc(
        filters=_get_valid_filters(filters),
        **SIINC_KWARGS,
    ) as client:
        posts: List[PubliiPostComparison] = client.sync(dry_run=True)
        if not posts:
            print("No matching posts found.")
            return

        for p in client.sync(dry_run=True):
            new_status: Optional[List[str]] = None
            if status:
                post_status_all: List[str] = [
                    x.strip() for x in p.status_all.split(",")
                ]
                if status in (StatusUpdate.published, StatusUpdate.draft):
                    new_status = [status.name] + [
                        x
                        for x in post_status_all
                        if x
                        not in (
                            status.name,
                            StatusUpdate.published.name,
                            StatusUpdate.draft.name,
                            StatusUpdate.trashed.name,
                        )
                    ]
                elif status in (
                    StatusUpdate.hidden,
                    StatusUpdate.trashed,
                    StatusUpdate.excluded,
                ):
                    new_status = [x for x in post_status_all if x != status.name] + [
                        status.name
                    ]
                else:
                    raise UnrecognizedStatusUpdateError(status.name)

            update_attrs: Dict[str, Any] = {}
            if date_published:
                update_attrs["created_at"] = date_published
            elif floor_date_published:
                update_attrs["created_at"] = millis_to_date(p.created_at)

            if date_modified:
                update_attrs["modified_at"] = date_modified
            if template:
                update_attrs["template"] = template
            if new_status:
                update_attrs["status"] = ",".join(new_status)

            client.update_post(post=p, dry_run=dry_run, **update_attrs)

    return _sync(filters=filters)


def _sync_watch_iteration(
    *args,
    watch_list: Optional[List[str]] = None,
    changes: Optional[Set[Tuple[Change, str]]] = None,
    **kwargs,
):
    diff_count_table: Optional[List[Dict[Any]]] = None
    if changes:
        diff_count: List[Tuple[Tuple[str, str], int]] = Counter(
            [
                (
                    path
                    if not watch_list
                    else "file"
                    if path.startswith(watch_list[0])
                    else "db",
                    change.name,
                )
                for change, path in changes
            ]
        ).most_common()
        diff_count_table = [
            {"source": x[0][0], "change": x[0][1], "count": x[1]} for x in diff_count
        ]
    section_char: str = random.choice(r"~@#$%*+\|/=zxo^v<>")
    print("\n" + (section_char * 80))

    print(
        section_char * 28,
        datetime.now().strftime(r" %Y-%m-%d %H:%M:%S "),
        section_char * 29,
    )
    print((section_char * 80) + "\n")
    if diff_count_table:
        print("Detected changes:")
        print("-" * 27)
        _print_data_table(diff_count_table)
        print("-" * 27)
        print()

    results = sync(*args, **kwargs)

    print((section_char * 80) + "\n")

    return results


@wraps(sync)
def sync_watch(*args: Any, **kwargs: Any) -> None:
    watch_list: List[str] = [
        str(SIINC_KWARGS["directory"]),
        str(SIINC_KWARGS["db"].parent),
    ]

    watch_list_str: str = "- " + "\n- ".join(watch_list)
    print(f"\nWatching:\n{watch_list_str}")

    results: List[PubliiPostComparison] = _sync_watch_iteration(*args, **kwargs)

    try:
        for changes in watch(
            *watch_list,
            debounce=3000,
            step=2000,
            rust_timeout=60000,
            yield_on_timeout=True,
            # force_polling=False,
            # poll_delay_ms=1000,
        ):
            _sync_watch_iteration(
                *args, watch_list=watch_list, changes=changes, **kwargs
            )
    except KeyboardInterrupt:
        print("Shutdown requested. ", end="")
    finally:
        print("Performing final sync.")
        results = _sync_watch_iteration(*args, **kwargs)

    return results


def main() -> None:
    resp: Optional[Any] = yapx.run(
        setup,
        sync,
        watch=sync_watch,
        ls=list_posts,
        list=list_posts,
        diff=list_posts_diffs,
        set=set_post_properties,
        _args=sys.argv[1:],
    )

    if resp is None:
        # cli run with no command; run sync by default.
        yapx.run(setup, diff=list_posts_diffs, _args=sys.argv[1:] + ["diff"])


if __name__ == "__main__":
    main()
