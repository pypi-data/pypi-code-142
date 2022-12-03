import datetime
import re
import shutil
import subprocess
from pathlib import Path
from typing import List, Tuple

from py_cover_letters.exceptions import CoverLetterException


def run_commands(commands: List[str], encoding: str = 'utf-8') -> Tuple[List[str], List[str]]:
    """
    Run command
    :param commands: <list> The command and parameters to run
    :param encoding: <str> Encoding for the shell
    :return: <tuple> Containing 2 lists. First one with results and the Second one with errors if any.
    """
    result = subprocess.run(commands,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    result_lines = result.stdout.decode(encoding).split('\n')[:-1]
    error_lines = result.stderr.decode(encoding).split('\n')[:-1]
    return result_lines, error_lines


def backup_file(filename: Path, backup_folder: Path, add_version: bool = True) -> Path:
    if not backup_folder.is_dir():
        error_message = f'Backup folder either is not a folder or does not exist.' \
                        f' Supplied: {backup_folder}. Type: {type(backup_folder)} exists: {backup_folder.exists()}'
        raise CoverLetterException(error_message)

    datetime_format = '%Y%m%d_%H%M%S'
    if add_version:
        from . import __version__ as current_version
        version_val = f'v{current_version}_'
    else:
        version_val = ''
    timestamp = datetime.datetime.now().strftime(datetime_format)
    backup_filename = backup_folder / f'{timestamp}_{version_val}{filename.name}'
    shutil.copy(filename, backup_filename)
    return backup_filename


def backup_excel(filename: Path, add_version: bool = True) -> Path:
    from py_cover_letters import CURRENT_CONFIGURATION
    backup_folder = Path(CURRENT_CONFIGURATION['database']['backup_folder'])
    backup_excel_file = backup_file(filename, backup_folder, add_version=add_version)
    return backup_excel_file


def get_libreoffice_version():
    which_cmd = ['which', 'libreoffice']
    results, errors = run_commands(which_cmd)
    if len(results) == 0:
        return 'Libreoffice not found.', False
    if len(errors) > 0:
        return 'Error running which command.', False

    regexp = re.compile(r"LibreOffice\s(?P<version>(\d\.\d\.\d\.?\d?)\s?(\d*)\(Build:\d+\))")
    command = ['libreoffice', '--version']
    results, errors = run_commands(command)
    if len(errors) > 0:
        return 'Errors running command libreoffice --version', False
    match = regexp.match(results[0])
    if match:
        return match.group('version'), True
    else:
        return results[0], False


def is_libreoffice_installed() -> bool:
    is_installed = False
    try:
        _, is_installed = get_libreoffice_version()
    except Exception:
        pass
    return is_installed
