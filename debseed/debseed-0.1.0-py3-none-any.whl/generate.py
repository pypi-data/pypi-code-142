from __future__ import annotations
import os, sys, shutil, subprocess, argparse, shutil, shlex, logging, jinja2
from pathlib import Path
from .utils import command, without_j2
from .settings import ORIGIN_ISO_DIR, PACKAGE_ASSETS, TARGET_ISO_DIR, ARCHIVES_ISO_DIR, Context, Edition, get_edition, get_editions, DEFAULT_EDITION
from .publish import publish as run_publish

logger = logging.getLogger(__name__)

TMP_DIR = Path("debseed.tmp")


def generate_add_arguments(parser: argparse.ArgumentParser):
    parser.add_argument('origin', help="name or path to the original Debian ISO file")
    parser.add_argument('edition', nargs='?', default=DEFAULT_EDITION, help="name of the edition: %s, or path to a preseed.cfg file" % (', '.join(edition + ('*' if edition == DEFAULT_EDITION else '') for edition in get_editions().keys())))
    parser.add_argument('--target', help="name or path to the target ISO file")
    parser.add_argument('--publish', '-p', action='store_true', help="publish generated ISO file to external store")
    parser.add_argument('--force', '-f', action='store_true', help="recreate the target ISO file if it already exists")
    parser.add_argument('--keep', '-k', action='store_true', help=f"keep temporary files")


@command(generate_add_arguments)
def generate(origin: str|Path, edition: str|Edition = None, target: str|Path = None, publish: bool = False, force: bool = False, keep = False) -> Path:
    """
    Generate a custom ISO file from an original Debian ISO file.

    Return path of target ISO file.
    """
    # Verify existency of xorriso
    if not shutil.which('xorriso'):
        logger.error("missing xorriso application")
        return None

    # Verify permissions
    file = PACKAGE_ASSETS.joinpath('late-command.sh')
    expected_perm = '755'
    actual_perm = oct(file.stat().st_mode)[-3:]
    if expected_perm != actual_perm:
        logger.error(f"invalid permissions on file {file}: {actual_perm} (expected {expected_perm}) - please ensure you're using a permission-aware filesystem")
        return None

    file = PACKAGE_ASSETS.joinpath('debian-cd-signing.gpg')
    expected_perm = '644'
    actual_perm = oct(file.stat().st_mode)[-3:]
    if expected_perm != actual_perm:
        logger.error(f"invalid permissions on file {file}: {actual_perm} (expected {expected_perm}) - please ensure you're using a permission-aware filesystem")
        return None

    # Prepare edition and preseed
    if isinstance(edition, Path):
        # 'edition' argument is considered to be a path to a preseed file
        preseed = edition
        edition = get_edition(DEFAULT_EDITION)
    
    elif isinstance(edition, str) and ('.' in edition or '/' in edition or '\\' in edition):
        # 'edition' argument is considered to be a path to a preseed file
        preseed = Path(edition)
        edition = get_edition(DEFAULT_EDITION)

    else:
        preseed = None
        if isinstance(edition, str):
            edition = get_edition(edition)

    # Prepare actual origin ISO file
    if isinstance(origin, str):
        if os.path.exists(origin):
            origin = Path(origin)
        else:
            origin = ORIGIN_ISO_DIR.joinpath(origin)
    
    if not origin.exists():
        logger.error(f"origin file not found: {origin}")
        return None

    # Extract context
    context = edition.get_context(origin.name)

    if not preseed:
        preseed = context.preseed_template

    # Prepare actual target ISO file
    if not target:
        target = context.target_iso

    elif isinstance(target, str):
        if '/' in target or '\\' in target:
            target = Path(context.format(target))
        else:
            target = TARGET_ISO_DIR.joinpath(context.format(target))

    if target.exists():
        if not force:
            logger.info("target ISO file already exists: %s, use --force to recreate" % target)
            return target
    elif (archive := ARCHIVES_ISO_DIR.joinpath(target.name)).exists():
        if not force:
            logger.info("target ISO file already exists in archives: %s, use --force to recreate" % archive)
            return target
    else:
        TARGET_ISO_DIR.mkdir(parents=True, exist_ok=True)

    # Prepare temporary directory
    tmp_dir = TMP_DIR.joinpath(target.stem)
    if tmp_dir.exists():
        _rmdir_with_chmod(tmp_dir)
    tmp_dir.mkdir(parents=True)

    # Prepare additional files
    prepared = []
    if context.late_command:
        tmp_path = tmp_dir.joinpath(without_j2(context.late_command.name))
        logger.info(f"prepare {tmp_path.name}")
        _prepare_file(context.late_command, tmp_path, context)
        prepared.append(tmp_path.name)

    if context.late_command_assets:
        tmp_path = tmp_dir.joinpath("late-command-assets")
        logger.info(f"prepare {tmp_path.name}")
        for assets in context.late_command_assets:
            _prepare_directory(assets, tmp_path, context)

        tmp_archive = tmp_dir.joinpath("late-command-assets.tgz")
        _run("tar", "-C", tmp_path, "-czf", tmp_archive, "--owner=0", "--group=0", ".", tag="tar (create %s)" % tmp_archive.name)
        prepared.append(tmp_archive.name)

    tmp_path = tmp_dir.joinpath("preseed.cfg")
    logger.info(f"prepare {tmp_path.name}")
    _prepare_file(preseed, tmp_path, context)
    prepared.append(tmp_path.name)

    # Prepare files for ISO
    tmp_extracted = tmp_dir.joinpath("extracted-iso")
    tmp_initrd = tmp_dir.joinpath("initrd")

    _run("xorriso", "-osirrox", "on", "-indev", origin, "-extract", "/", tmp_extracted, tag="xorriso (extract %s)" % origin)
    _run("chmod", "+w", "-R", f"{tmp_extracted}/install.amd", capture=True)

    _run("bash", "-c", f"gunzip -c {tmp_extracted}/install.amd/initrd.gz > {tmp_initrd}", tag="gunzip (uncompress initrd)")

    _run("bash", "-c", f"(cd {tmp_dir}; find {' '.join(shlex.quote(p) + ' ' for p in prepared)} -type f | cpio -H newc -o -A -F {tmp_initrd.name})", tag="cpio (add prepared files to initrd)")

    _run("bash", "-c", f"gzip -c {tmp_initrd} > {tmp_extracted}/install.amd/initrd.gz", tag="gzip (compress initrd)")
    _run("chmod", "-w", "-R", f"{tmp_extracted}/install.amd", capture=True)

    _run("chmod", "+w", f"{tmp_extracted}/md5sum.txt", capture=True)
    _run("bash", "-c", f"(cd {tmp_extracted}; find -follow -type f ! -name md5sum.txt -print0 | xargs -0 md5sum > md5sum.txt)", tag="md5sum")
    _run("chmod", "-w", f"{tmp_extracted}/md5sum.txt", capture=True)

    # Create ISO file
    args = ["xorriso", "-as", "mkisofs", "-o", target]
        
    if context.target_iso_volid:
        args += ["-volid", context.target_iso_volid]
    if context.target_iso_volset:
        args += ["--volset", context.target_iso_volset]
    if context.target_iso_preparer:
        args += ["--preparer", context.target_iso_preparer]
    if context.target_iso_publisher:
        args += ["--publisher", context.target_iso_publisher]

    args += [
        "-isohybrid-mbr", "/usr/lib/ISOLINUX/isohdpfx.bin",
        "-c", "isolinux/boot.cat", "-b", "isolinux/isolinux.bin", "-no-emul-boot",
        "-boot-load-size", "4", "-boot-info-table", tmp_extracted
    ]

    _run(*args, tag="xorriso (create %s)" % target)


    # Clean temporary directory
    if keep:
        logger.info("temporary directory kept: %s", tmp_dir)
    else:
        logger.debug("clean temporary directory: %s", tmp_dir)
        _rmdir_with_chmod(tmp_dir)
        if not any(TMP_DIR.iterdir()):
            logger.debug("clean temporary container: %s", TMP_DIR)
            TMP_DIR.rmdir()

    # Publish
    if publish:
        run_publish(target, force=force)

    return target


def _run(*args, tag=None, capture=False):
    if not tag:
        tag = args[0]

    if capture:
        logger.debug(f"run {tag} {args}")
        cp = subprocess.run(args, text=True, capture_output=True)
        
        if value := cp.stdout.strip():
            logger.info(f"command {tag} stdout: {value}")

        if value := cp.stderr.strip():
            logger.info(f"command {tag} stderr: {value}")
    
    else: # live
        logger.info(f"run {tag}")
        logger.debug("%s args: %s", tag, args)
        cp = subprocess.run(args, text=True, stdout=sys.stdout, stderr=sys.stderr)
    

    if cp.returncode != 0:
        raise ValueError(f"command {tag} returned code {cp.returncode}")


def _rmdir_with_chmod(path):
    os.system(f"chmod +rw -R \"{path}\"")
    shutil.rmtree(path)


def _prepare_file(origin: Path, target: Path, context: Context):
    # copy including timestamps and permissions/executable
    shutil.copy2(str(origin), str(target))

    if origin.name.endswith(".j2"):
        with open(target, "w") as f:
            f.write(_render_template(origin, context))


def _prepare_directory(origin_dir: Path, target_dir: Path, context: Context):
    if not target_dir.exists():
        target_dir.mkdir()

    for path in origin_dir.iterdir():
        target = target_dir.joinpath(without_j2(path.name))
        if path.is_dir():
            _prepare_directory(path, target, context)
        elif not target.exists():
            _prepare_file(path, target, context)


def _render_template(template: str|Path, context: Context) -> str:
    try:
        with open(template) as f:
            return jinja2.Template(f.read()).render(**context.template_data)
    except Exception as e:
        raise ValueError(f"cannot render template {template}: {e}")
