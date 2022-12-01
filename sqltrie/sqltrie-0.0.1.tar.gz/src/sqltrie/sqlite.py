import sqlite3
from functools import cached_property

from .trie import AbstractTrie, ShortKeyError

ROOT_ID = 1
ROOT_NAME = "/"

class SQLiteTrie(AbstractTrie):
    def __init__(self, *args, root_id=None, **kwargs):
        self._root_id = root_id or ROOT_ID

    #        super().__init__(*args, **kwargs)

    @cached_property
    def _conn(self):
        conn = sqlite3.connect(":memory:")
        conn.row_factory = sqlite3.Row
        conn.executescript(
            """
            CREATE TABLE nodes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pid INTEGER,
                name TEXT,
                value TEXT,
                UNIQUE(pid, name)
            );
            CREATE INDEX nodes_pid_idx ON nodes (pid);
            INSERT INTO nodes (id, pid, name, value) VALUES (1, NULL, '/', NULL)
            """
        )
        return conn

    def _create_node(self, key):
        pid = self._root_id
        for name in key:
            ret = self._conn.execute(
                """
                SELECT id FROM nodes WHERE nodes.pid = ? AND nodes.name = ?
                """,
                (pid, name),
            ).fetchone()
            if ret is None:
                self._conn.execute(
                    """
                    INSERT OR IGNORE INTO nodes (pid, name) VALUES (?, ?)
                    """,
                    (pid, name),
                )
                # FIXME this might not work on IGNORE
                ret = self._conn.execute(
                    "SELECT last_insert_rowid() AS id"
                ).fetchone()
            pid = ret["id"]
        return pid

    def _traverse(self, key):
        # FIXME rename to walk_towards or something?

        steps = ", ".join(
            f"({idx + 1}, '{key[idx]}')"
            for idx in range(len(key))
        )

        rows = self._conn.execute(
            f"""
            WITH RECURSIVE
                mysteps (depth, name) AS (
                    VALUES {steps}
                ),
                myfunc (id, pid, name, value, depth) AS (
                    SELECT nodes.id, nodes.pid, nodes.name, nodes.value, mysteps.depth
                    FROM nodes, mysteps
                    WHERE mysteps.depth == 1 AND nodes.pid == ? AND nodes.name == mysteps.name

                    UNION ALL

                    SELECT nodes.id, nodes.pid, nodes.name, nodes.value, myfunc.depth + 1
                    FROM nodes, myfunc, mysteps
                    WHERE nodes.pid == myfunc.id AND mysteps.depth == myfunc.depth + 1 AND mysteps.name == nodes.name
                )
            SELECT id, pid, name, value FROM myfunc
            """,
            (self._root_id,),
        )

        yield from rows

    def _get_node(self, key):
        if not key:
            return {
                "id": self._root_id,
                "pid": None,
                "name": None,
                "value": None,
            }

        rows = list(self._traverse(key))
        if len(rows) != len(key):
            raise KeyError(key)

        return rows[-1]

    def _get_children(self, key, limit=None):
        node = self._get_node(key)

        limit_sql = ""
        if limit:
            limit_sql = f"LIMIT {limit}"

        return self._conn.execute(
            f"""
            SELECT * FROM nodes WHERE nodes.pid == ? {limit_sql}
            """,
            (node["id"],),
        ).fetchall()

    def _delete_node(self, key):
        node = self._get_node(key)
        self._conn.execute(
            """
            DELETE FROM nodes WHERE id = ?
            """,
            (node["id"],),
        )

    def __setitem__(self, key, value):
        nid = self._create_node(key)
        self._conn.execute(
            """
            UPDATE nodes SET value = ? WHERE id = ?
            """,
            (
                value,
                nid,
            ),
        )

    def __getitem__(self, key):
        return self._get_node(key)["value"]

    def __delitem__(self, key):
        node = self._get_node(key)
        self._conn.execute(
            f"""
            UPDATE nodes SET value = NULL WHERE id == ?
            """,
            (node["id"],),
        )

    def __len__(self):
        return self._conn.execute(
            """
            SELECT COUNT(*) AS count FROM nodes WHERE nodes.value is not  NULL
            """
        ).fetchone()["count"]

    def longest_prefix(self, key):
        return tuple([row["name"] for row in self._traverse(key)])

    def _get_key(self, nid):
        rows = self._conn.execute(
            """
            WITH RECURSIVE
                myfunc (pid, name) AS (
                    SELECT nodes.pid, nodes.name FROM nodes WHERE nodes.id == ?

                    UNION ALL

                    SELECT nodes.pid, nodes.name FROM nodes, myfunc WHERE nodes.id == myfunc.pid AND nodes.id != ?
                )
            SELECT myfunc.name FROM myfunc
            """,
            (nid, self._root_id),
        ).fetchall()

        return tuple(reversed([row["name"] for row in rows]))

    def iteritems(self, prefix=None, shallow=False):
        assert not shallow
        if prefix:
            pid = self._get_node(prefix)["id"]
        else:
            pid = self._root_id

        rows = self._conn.execute(
            """
            WITH RECURSIVE
                myfunc (id, pid, name, value) AS (
                    SELECT * FROM nodes WHERE nodes.pid == ?

                    UNION ALL

                    SELECT nodes.id, nodes.pid, myfunc.name || '/' || nodes.name, nodes.value
                    FROM nodes, myfunc WHERE myfunc.id == nodes.pid
                )
            SELECT * FROM myfunc
            """,
            (pid,),
        )

        yield from (
            (tuple(row["name"].split("/")), row["value"])
            for row in rows
        )

    def clear(self):
        self._conn.execute("DELETE FROM nodes")

    def diff(self, old_key, new_key, with_unchanged=False):
        old_node = self._get_node(old_key)
        new_node = self._get_node(new_key)

        if not with_unchanged:
            where = "WHERE diff_dir.old_id != NULL and diff_dir.new_id != NULL"

        rows = self._conn.execute(
            f"""
            WITH RECURSIVE
                old_root AS (
                    SELECT ? AS id
                ),
                new_root AS (
                    SELECT ? AS id
                ),
                old_children AS (
                    SELECT nodes.* FROM nodes, old_root WHERE nodes.pid == old_root.id

                    UNION ALL

                    SELECT nodes.* FROM nodes, old_children WHERE nodes.pid == old_children.id
                ),
                new_children AS (
                    SELECT nodes.* FROM nodes, new_root WHERE nodes.pid == new_root.id

                    UNION ALL

                    SELECT nodes.* FROM nodes, new_children WHERE nodes.pid == new_children.id
                ),
                diff_dir (old_id, old_pid, old_name, old_value, new_id, new_pid, new_name, new_value) AS (
                    /* FULL OUTER JOIN is not supported, so we have to use two LEFT JOINs :( */
                    SELECT old.id, old.pid, old.name, old.value, new.id, new.pid, new.name, new.value
                    FROM
                    old_children old LEFT JOIN new_children new ON old.name == new.name
                    UNION
                    SELECT old.id, old.pid, old.name, old.value, new.id, new.pid, new.name, new.value
                    FROM
                    new_children new LEFT JOIN old_children old ON old.name == new.name
                )
                SELECT * FROM diff_dir {where}
            """,
            (old_node["id"], new_node["id"]),
        )

        yield from (
            (tuple(row["name"].split("/")), row["value"])
            for row in rows
        )
