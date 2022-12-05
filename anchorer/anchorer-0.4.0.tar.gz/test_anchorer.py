from typing import List

import subprocess
from pathlib import Path

from stevedore import ExtensionManager


def test_extension_available():
    """The pre_mkvirtualenv hook is available as an entrypoint and extension."""

    def on_load_failure_callback(manager, entry_point, error):
        raise

    # raise an exception if unable to load any plugin, as usually they'd be quietly skipped
    manager = ExtensionManager('virtualenvwrapper.pre_mkvirtualenv', on_load_failure_callback=on_load_failure_callback)

    # make sure the plugin is in the entry points
    assert {'anchorer'} < set(manager.entry_points_names())

    # make sure the plugin is available in the extensions
    assert {'anchorer'} < set(manager.map(lambda extension: extension.name))


def assert_all_resolved(paths: List[Path]):
    """Assert that all paths given are resolved, or empty.

    Empty is allowed, assuming that the current working directory is set to be an absolute path, the
    """
    assert not [p for p in paths if str(p) != '.' and p.resolve() != p]


def test_virtualenvwrapper_plugin(tmp_path, monkeypatch):
    """Links are resolved within the environments."""

    def env_directory(env: str) -> str:
        return tmp_path / env

    def evaled(env: str, code: str):
        directory = env_directory(env)
        return eval(subprocess.check_output([directory / "bin/python", "-c", code],
                                            cwd=directory))

    subprocess.run(['python', '-m', 'virtualenvwrapper.hook_loader', 'pre_mkvirtualenv'])

    monkeypatch.setenv('WORKON_HOME', str(tmp_path))
    # make test-env
    subprocess.check_call(['bash', '-c', 'source virtualenvwrapper.sh; mkvirtualenv test-env'])
    # make link-env which is just a symlink to test-env
    (tmp_path / 'link-env').symlink_to(tmp_path / 'test-env')

    # check that the paths have been resolved
    pythonpath = list(map(Path, evaled("link-env", "import sys; print(sys.path)")))
    assert_all_resolved(pythonpath)
    cwd = Path(evaled("link-env", "import os; print(repr(os.getcwd()))"))
    assert cwd == env_directory('test-env')
