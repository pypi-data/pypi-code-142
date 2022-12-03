import shlex
import qqr
import time


def test_version(script_runner):
    command = "qqr --version"
    start = time.time()
    ret = script_runner.run(*shlex.split(command))
    end = time.time()
    elapsed = end - start
    assert ret.success
    assert qqr.__version__ in ret.stdout
    assert ret.stderr == ""
    # make sure it took less than a second
    assert elapsed < 1.0
