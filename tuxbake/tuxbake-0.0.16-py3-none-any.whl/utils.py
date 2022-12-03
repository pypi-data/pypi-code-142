import os
import sys
import subprocess
from pathlib import Path
from tuxbake.exceptions import TuxbakeRunCmdError, TuxbakeParsingError
from tuxmake.logging import debug
import logging

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


__log_flag__ = False


def log_handler(func):
    """
    Logging decorator which toggles the log_flag to enable logging for the decorated function.
    """

    def log(*args, **kwargs):
        src_dir = args[0].src_dir
        fh = logging.FileHandler(f"{src_dir}/fetch.log")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        global __log_flag__
        __log_flag__ = True
        value = func(*args, **kwargs)
        __log_flag__ = False

        return value

    return log


@log_handler
def repo_init(oebuild, src_dir, local_manifest=None, pinned_manifest=None):
    cmd = f"repo init -u {oebuild.repo.url} -b {oebuild.repo.branch} -m {oebuild.repo.manifest}".split()
    run_cmd(cmd, src_dir)
    if pinned_manifest:
        cmd = f"cp {pinned_manifest} .repo/manifests/{oebuild.repo.manifest}".split()
        run_cmd(cmd, src_dir)

    if local_manifest:
        cmd = f"mkdir -p .repo/local_manifests/".split()
        run_cmd(cmd, src_dir)
        cmd = f"cp {local_manifest} .repo/local_manifests/".split()
        run_cmd(cmd, src_dir)
    cmd = "repo sync -j16".split()
    run_cmd(cmd, src_dir)
    cmd = "repo manifest -r -o pinned-manifest.xml".split()
    run_cmd(cmd, src_dir)


def git_fetch(what_to_fetch, src_dir, dir_path):
    cmd = f"git fetch origin --quiet {what_to_fetch}".split()
    run_cmd(cmd, os.path.join(src_dir, dir_path))


def git_get_sha(branch, url):
    cmd = f"git ls-remote --exit-code --quiet {url} {branch}".split()
    try:
        ret = run_cmd(cmd, None)
    except:
        raise TuxbakeRunCmdError(f"Unable to fetch the 'branch' or 'ref': {branch}")
    sha = ret.out.split()[0].decode("utf-8")
    return sha


@log_handler
def git_init(oebuild, src_dir):
    for git_object in oebuild.git_trees:
        url = git_object.url.rstrip("/")
        branch = git_object.branch or git_object.ref
        sha = git_object.sha or git_get_sha(branch, url)
        dest = git_object.dest
        if not (branch or sha):
            raise TuxbakeRunCmdError(
                f"One of branch/ref/sha should be specified for {git_object} {url}"
            )
        basename = os.path.splitext(os.path.basename(url))[0]
        # set to basename as when dest not present can be used to create source folder using basename inside src_dir
        dir_path = basename
        if dest:
            # checks ( handled ~ and ../../ )
            resolved_abs_dest = (
                os.path.abspath(os.path.join(src_dir, os.path.expanduser(dest)))
                + os.sep
            )
            if resolved_abs_dest.startswith(os.path.abspath(src_dir) + os.sep):
                dir_repo = Path(os.path.join(resolved_abs_dest, basename))
                dir_path = dir_repo
            else:
                raise TuxbakeParsingError(
                    f"Dest path provided in git_trees must be relative to src_dir: {src_dir}, curr dest: {resolved_abs_dest}"
                )
        else:
            dir_repo = Path(os.path.join(src_dir, basename))

        if not dir_repo.exists() and not dir_repo.is_dir():
            cmd = f"mkdir -p {dir_path}".split()
            run_cmd(cmd, src_dir)
            cmd = f"git init --quiet .".split()
            run_cmd(cmd, os.path.join(src_dir, dir_path))
            cmd = f"git remote add origin {url}".split()
            run_cmd(cmd, os.path.join(src_dir, dir_path))

        git_fetch(sha, src_dir, dir_path)
        cmd = f"git checkout {sha}".split()
        run_cmd(cmd, os.path.join(src_dir, dir_path))


def find_bitbake_env(env_file, key):
    with open(env_file) as env:
        for line in env.readlines():
            if line.startswith(f"{key}="):
                return line.split("=")[1].strip().replace('"', "")


def copy_artifacts(artifacts, src_dir, artifacts_dir, bitbake_env_file):
    if not os.path.exists(bitbake_env_file):
        return
    deploy_dir = find_bitbake_env(bitbake_env_file, "DEPLOY_DIR")
    if deploy_dir:
        if artifacts:
            dir_paths = [f"{deploy_dir}/{artifact}" for artifact in artifacts]
            dirs = " ".join(dir_paths)
        else:
            # whole DEPLOY_DIR to be published
            dirs = f"{deploy_dir}/."

        if not os.path.exists(artifacts_dir):
            os.makedirs(artifacts_dir)
        else:
            cmd = f"rm -rf {artifacts_dir}".split()
            run_cmd(cmd, src_dir)
            cmd = f"mkdir -p {artifacts_dir}".split()
            run_cmd(cmd, src_dir)
        cmd = f"cp -R {dirs} {artifacts_dir}".split()
        run_cmd(cmd, src_dir, fail_ok=True)
        # copy bitbake-environment files as well
        cmd = f"cp -R {bitbake_env_file} {artifacts_dir}".split()
        run_cmd(cmd, src_dir, fail_ok=True)


def run_cmd(cmd, src_dir, env=None, fail_ok=False):
    msg = f"Running cmd: '{cmd}' in '{src_dir}'"
    debug(msg)
    process = subprocess.Popen(
        cmd, cwd=src_dir, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    process.out, process.err = process.communicate()
    handle_log([msg, process.out, process.err])
    if not fail_ok and process.returncode != 0:
        raise TuxbakeRunCmdError(f"Failed to run: {' '.join(cmd)}")
    return process


def handle_log(logs_list):
    global __log_flag__
    # process.err
    err = logs_list[-1]
    if err:
        print(err.decode("utf-8") if isinstance(err, bytes) else err, file=sys.stderr)

    if __log_flag__:
        for data in logs_list:
            if not data:
                continue
            elif isinstance(data, bytes):
                logger.info(data.decode("utf-8"))
            else:
                logger.info(data)
    return
