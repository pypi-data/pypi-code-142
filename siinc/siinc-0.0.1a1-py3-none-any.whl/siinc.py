import os
import sqlite3
from collections import Counter
from datetime import date, datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from .exceptions import DuplicateSlugError, MisplacedFileError, OrphanFileError
from .models import ComparisonResult, PubliiPost, PubliiPostComparison, ValidFilters
from .utils import (
    datetime_to_millis,
    get_public_vars,
    millis_to_datetime,
    tabulate_dict,
)


class Siinc:
    def __init__(
        self,
        db: Path,
        directory: Path,
        path_format: Optional[str] = r"{status}/{tag}/{author}/{date}",
        path_date_format: Optional[str] = None,
        filters: Optional[ValidFilters] = None,
        privileged: bool = False,
        delete_orphans: bool = False,
        force_push: bool = False,
        force_pull: bool = False,
    ):
        self._conn: sqlite3.Connection = sqlite3.connect(db)

        self._dir: Path = directory
        self._dir.mkdir(exist_ok=True)

        self._path_format: str = path_format if path_format else ""
        self._path_date_format: str = path_date_format if path_date_format else ""

        self._force_push: bool = force_push
        self._force_pull: bool = force_pull

        self._filters = (
            filters
            if filters and any(v for v in get_public_vars(filters).values())
            else None
        )
        self._privileged = privileged
        self._delete_orphans = delete_orphans

        self._posts = self._refresh_posts()
        self._files = self._refresh_files()

    def __enter__(self) -> "Siinc":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

    def close(self) -> None:
        self._conn.close()

    def get_files(self) -> Dict[str, Path]:
        return self._files

    def get_file(self, slug: str) -> Optional[Path]:
        return self._files.get(slug)

    def get_posts(self) -> Dict[str, PubliiPost]:
        return self._posts

    def get_post(self, slug: str) -> Optional[PubliiPost]:
        return self._posts.get(slug)

    def _build_expected_file_path(
        self,
        post: PubliiPost,
    ) -> Path:
        return self._dir.joinpath(
            self._path_format.format(
                status=post.status,
                tag=post.main_tag,
                author=post.author,
                date=millis_to_datetime(post.created_at).strftime(
                    self._path_date_format
                ),
            )
        ).joinpath(f"{post.slug}.{post.text_format}")

    def _refresh_posts(
        self,
    ) -> Dict[str, PubliiPost]:
        sql_qry: str = r"""
select
p.id
, p.slug
, a.username as author
, p.created_at
, coalesce(p.modified_at, p.created_at) as modified_at
, case
    when (p.status like 'trashed%' or p.status like '%,trashed%') then 'trashed'
    when (p.status like 'draft%' or p.status like '%,draft%') then 'draft'
    when (p.status like 'hidden%' or p.status like '%,hidden%') then 'hidden'
    when (p.status like 'published%' or p.status like '%,published%') then 'published'
    else p.status
end as status
, p.status as status_all
--, p_view.value as view_settings
, coalesce(coalesce(t_main.slug, t.slug), "_untagged_") as main_tag
, case json_extract(p_meta.value, '$.editor')
    when 'markdown' then 'md'
    when 'blockeditor' then 'json'
    else 'html'
end as text_format
, p.text
from posts as p
left join posts_additional_data as p_meta
on p.id = p_meta.post_id
and p_meta.key = '_core'
--left join posts_additional_data as p_view
--on p.id = p_view.post_id
--and p_view.key = 'postViewSettings'
left join authors a
on cast(p.authors as int) = a.id
left join (
select
post_id
, min(tag_id) as tag_id
from posts_tags
group by post_id
) as pt
on p.id = pt.post_id
left join tags t
on pt.tag_id = t.id
left join tags t_main
on cast(json_extract(p_meta.value, '$.mainTag') as int) = t_main.id
order by coalesce(modified_at, created_at) desc
            """
        sql: sqlite3.Cursor = self._conn.cursor()
        try:
            self._posts = {
                p.slug: p
                for x in sql.execute(sql_qry)
                for p in [PubliiPost(*x)]
                # TODO: use filters directly in SQL for better perf.
                if not self._filters
                or (
                    (not self._filters.tag or p.main_tag == self._filters.tag)
                    and (not self._filters.slug or p.slug == self._filters.slug)
                    and (not self._filters.status or p.status == self._filters.status)
                )
            }
            return self.get_posts()
        finally:
            sql.close()

    def _refresh_files(
        self,
    ) -> Dict[str, Path]:
        found_files: List[Path] = [
            p
            for r, _, f in os.walk(self._dir)
            for x in f
            for p in [Path(r).joinpath(x)]
        ]
        orphan_files: List[Path] = [
            x for x in found_files if x.stem not in self.get_posts()
        ]
        if orphan_files:
            if not self._filters:
                if not self._privileged or not self._delete_orphans:
                    raise OrphanFileError(
                        f"Found {len(orphan_files)} orphaned files."
                        f" To remediate, run: `siinc -px list`"
                    )
                for x in orphan_files:
                    x.unlink()

            # if self._orphan_file_policy == OrphanFilePolicy.IGNORE:
            found_files = [x for x in found_files if x not in orphan_files]

        dupe_slugs: List[str] = [
            s for s, n in Counter(x.stem for x in found_files).most_common() if n > 1
        ]
        if dupe_slugs:
            raise DuplicateSlugError(f"Duplicate slugs found: {dupe_slugs}")

        self._files = {x.stem: x for x in found_files}
        return self.get_files()

    def _remove_empty_dirs(self) -> None:
        c: int = 0
        for p, d, f in os.walk(self._dir):
            if p != self._dir and not d and not f:
                os.rmdir(p)
                c += 1

        if c > 0:
            self._remove_empty_dirs()

    def _organize_files(self) -> List[PubliiPostComparison]:
        comparison: List[PubliiPostComparison] = self._compare()

        c: int = 0
        for x in comparison:
            if x.file_path and x.file_path != x.file_path_expected:
                print(
                    f"Moving: '{x.file_path.relative_to(self._dir)}'"
                    f" --> '{x.file_path_expected.relative_to(self._dir)}'"
                )
                x.file_path_expected.parent.mkdir(parents=True, exist_ok=True)
                x.file_path.rename(x.file_path_expected)
                c += 1

        if c > 0:
            self._remove_empty_dirs()
            self._refresh_files()
            comparison = self._compare()

        return comparison

    def update_post(
        self, post: PubliiPost, dry_run: bool = False, **kwargs: Any
    ) -> None:
        if not kwargs:
            print(f"{post.slug} --> Nothing to update")
        elif dry_run:
            print(f"{post.slug} --> {kwargs}")
        else:
            for k in list(kwargs):
                v = kwargs[k]
                if isinstance(v, (date, datetime)):
                    kwargs[k] = datetime_to_millis(v)

            sql_cmd: str = (
                f"update posts set"
                f" {', '.join(k+' = ?' for k in kwargs)}"
                f" where id = ?"
            )
            cur: sqlite3.Cursor = self._conn.cursor()
            try:
                cur.execute(sql_cmd, (*kwargs.values(), post.id))
                self._conn.commit()
            finally:
                cur.close()

    def _compare(self) -> List[PubliiPostComparison]:
        return [
            post.compare(
                file_path_expected=self._build_expected_file_path(post),
                file_path_actual=self.get_file(slug),
                force_pull=self._force_pull,
                force_push=self._force_push,
            )
            for slug, post in self.get_posts().items()
        ]

    def sync(
        self,
        dry_run: bool = False,
    ) -> List[PubliiPostComparison]:

        comparison: List[PubliiPostComparison] = (
            self._organize_files() if self._privileged else self._compare()
        )
        misplaced_files: List[PubliiPostComparison] = [
            x for x in comparison if x.file_path and x.file_path != x.file_path_expected
        ]
        if misplaced_files:
            data_table: List[Dict[str, Optional[Path]]] = [
                {
                    "FOUND": x.file_path.relative_to(self._dir),
                    "EXPECTED": x.file_path_expected.relative_to(self._dir),
                }
                for x in misplaced_files
            ]
            raise MisplacedFileError(
                f"Found {len(misplaced_files)} misplaced files."
                f"\n{tabulate_dict(data_table)}"
                f"\n\n> To remediate, run: `siinc -p list`\n"
            )

        # TODO: add safeguard; refuse to push if all local files are newer.
        # if not self._filters and all(
        #     x.result == ComparisonResult.push for x in comparison
        # ):
        #     ...
        if self._filters and self._filters.result:
            comparison = [x for x in comparison if x.result == self._filters.result]

        if dry_run:
            return comparison

        for x in comparison:
            if x.result == ComparisonResult.pull:
                if not x.file_path:
                    x.file_path_expected.parent.mkdir(parents=True, exist_ok=True)
                x.file_path_expected.write_text(x.text)

                mod_time: float = x.modified_at / 1000
                os.utime(str(x.file_path_expected), (mod_time, mod_time))
            elif x.result == ComparisonResult.push:
                self.update_post(
                    post=x,
                    text=x.file_text,
                    modified_at=x.file_modified_at,
                )
            # if x.result in [
            #     ComparisonResult.EQUAL,
            #     ComparisonResult.IGNORE,
            #     ComparisonResult.CONFLICT,
            # ]:
            #     continue

        return comparison
