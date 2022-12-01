import os
import re
import traceback
from typing import Optional

import duckdb
from ipykernel.kernelbase import Kernel


class DuckDBKernel(Kernel):
    implementation = 'DuckDB'
    implementation_version = '0.6.0'
    banner = 'DuckDB Kernel'
    language_info = {
        'name': 'duckdb',
        'mimetype': 'application/sql',
        'file_extension': '.sql',
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._db: Optional[duckdb.DuckDBPyConnection] = None

    # output related functions
    def print(self, text: str, name: str = 'stdout'):
        self.send_response(self.iopub_socket, 'stream', {
            'name': name,
            'text': text
        })

    def print_exception(self, e: Exception):
        if isinstance(e, AssertionError):
            text = str(e)
        elif isinstance(e, (duckdb.OperationalError, duckdb.ProgrammingError)):
            text = str(e)
        else:
            text = traceback.format_exc()

        self.print(text, 'stderr')

    def print_data(self, *data: str, mime: str = 'text/html'):
        for v in data:
            self.send_response(self.iopub_socket, 'display_data', {
                'data': {
                    mime: v
                },
                # `metadata` is required. Otherwise, Jupyter Lab does not display any output.
                # This is not the case when using Jupyter Notebook btw.
                'metadata': {}
            })

    # database related functions
    def _load_database(self, database: str, read_only: bool):
        if self._db is None:
            self._db = duckdb.connect(database, read_only)
            return True
        else:
            return False

    def _unload_database(self):
        if self._db is not None:
            self._db.close()
            self._db = None
            return True
        else:
            return False

    def _execute_stmt(self, query: str, silent: bool):
        if self._db is None:
            raise AssertionError('load a database first')

        with self._db.cursor() as cursor:
            cursor.execute(query)

            if not silent:
                # table header
                table_header = ''.join(map(lambda e: f'<th>{e[0]}</th>', cursor.description))

                # table data
                rows = cursor.fetchall()

                table_data = ''.join(map(
                    lambda row: '<tr>' + ''.join(map(lambda e: f'<td>{e}</td>', row)) + '</tr>',
                    rows
                ))

                # send to client
                self.print_data(f'''
                    <table class="duckdb-query-result">
                        {table_header}
                        {table_data}
                    </table>
                ''')

                self.print_data(f'{len(rows)} row{"" if len(rows) == 1 else "s"}')

    # magic command related functions
    def _load_magic(self, silent: bool, target: str, create: bool, source: str = None):
        # unload current database if necessary
        if self._unload_database():
            if not silent:
                self.print('unloaded database\n')

        # load new database
        if target.startswith(("'", '"')):
            target = target[1:-1]

        if create and os.path.exists(target):
            os.remove(target)

        if self._load_database(target, read_only=False):
            if not silent:
                self.print(f'loaded database {target}\n')

        # copy data from source database
        if source is not None:
            if source.startswith(("'", '"')):
                source = source[1:-1]

            if source.endswith('.sql'):
                with open(source, 'r') as file:
                    content = file.read()

                    # statements = re.split(r';\r?\n', content)
                    # for statement in statements:
                    #     self._db.execute(statement)

                    self._db.execute(content)

                    if not silent:
                        self.print(f'executed {source}')

            else:
                with duckdb.connect(source, read_only=True) as source_db:
                    source_db.execute('SHOW TABLES')
                    for table, in source_db.fetchall():
                        transfer_df = source_db.query(f'SELECT * FROM {table}').to_df()
                        self._db.execute(f'CREATE TABLE {table} AS SELECT * FROM transfer_df')

                        if not silent:
                            self.print(f'transferred table {table}\n')

    def handle_magic(self, code: str, silent: bool):
        if code.lower().startswith('%load'):
            # parse line
            match = re.match(r'''^%LOAD +([^ ]+?|'.+?'|".+?")$''',
                             code.strip(), re.IGNORECASE)
            if match is None:
                raise AssertionError('usage: %LOAD target.db')

            # call
            self._load_magic(silent, match.group(1), False)

        elif code.lower().startswith('%create'):
            # parse line
            match = re.match(r'''^%CREATE +([^ ]+?|'.+?'|".+?")( +FROM +([^ ]+?|'.+?'|".+?"))?$''',
                             code.strip(), re.IGNORECASE)
            if match is None:
                raise AssertionError('usage: %CREATE target.db [FROM source.db]')

            # call
            self._load_magic(silent, match.group(1), True, match.group(3))

        else:
            raise AssertionError('unknown magic command')

    # jupyter related functions
    def do_execute(self, code: str, silent: bool,
                   store_history: bool = True, user_expressions: dict = None, allow_stdin: bool = False,
                   **kwargs):
        try:
            # handle magic commands
            if code.startswith('%'):
                self.handle_magic(code, silent)

            # execute statement otherwise
            else:
                self._execute_stmt(code, silent)

            return {
                'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {}
            }

        except Exception as e:
            self.print_exception(e)

            return {
                'status': 'error',
                'ename': str(type(e)),
                'evalue': str(e),
                'traceback': traceback.format_exc()
            }

    def do_shutdown(self, restart):
        self._unload_database()
        return super().do_shutdown(restart)
