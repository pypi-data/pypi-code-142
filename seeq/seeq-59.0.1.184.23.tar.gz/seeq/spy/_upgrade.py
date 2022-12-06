from __future__ import annotations

import re
from typing import Optional

import IPython

from seeq import spy
from seeq.spy import _common, _login, Session, Status, _datalab
from seeq.spy._errors import *


def upgrade(version: Optional[str] = None, force_restart: bool = False, status: Optional[Status] = None,
            session: Optional[Session] = None):
    """
    Upgrades to the latest version of SPy that is compatible with this version of Seeq Server.

    An internet connection is required since this uses pip to pull the latest version from PyPI. This must be
    invoked from a Jupyter notebook or other IPython-compatible environment. The kernel will automatically be
    restarted when the upgrade is complete.

    Parameters
    ----------
    version : str, optional
        Attempts to upgrade to the provided version exactly as specified. The full SPy version must be
        provided (E.G. 58.0.2.184.12).

    force_restart : bool, optional
        If True, forces the kernel to shut down and restart after the upgrade. All in-memory variables and
        imports will be lost.

    status : spy.Status, optional
        If specified, the supplied Status object will be updated as the command progresses. It gets filled
        in with the same information you would see in Jupyter in the blue/green/red table below your code
        while the command is executed.

    session : spy.Session, optional
        If supplied, the Session object (and its Options) will be used to store the login session state.
        This is used to access the server's current version.

    Examples
    --------
    Upgrade to the latest version of SPy compatible with your Seeq server's major version.
    >>> spy.upgrade()

    Upgrade to version '58.0.2.184.12' of SPy.
    >>> spy.upgrade(version='58.0.2.184.12')

    """
    _common.validate_argument_types([
        (version, 'version', str),
        (status, 'status', Status),
        (session, 'session', Session),
    ])
    status = Status.validate(status)

    exact_match_version = False
    if version:
        exact_match_version = True
    else:
        session = Session.validate(session)
        _login.validate_login(session, status)
        seeq_server_major, seeq_server_minor, _ = _login.get_server_version_tuple(session)
        version = f'{seeq_server_major}.{seeq_server_minor}'

    if version is None:
        raise SPyValueError('Unable to determine Seeq Server version')

    if 'r' in version.lower():
        version = re.sub(pattern='r', repl='', string=version, flags=re.IGNORECASE)

    pip_command = _login.generate_pip_upgrade(version, exact_match_version)

    ipython = IPython.get_ipython()
    if not _datalab.is_ipython() or not _datalab.is_ipython_interactive() or not ipython:
        raise SPyValueError(f'spy.upgrade() must be invoked from a Jupyter notebook or other IPython-compatible '
                            f'environment. Unable to run "{pip_command}".')
    restart_message = 'The kernel will automatically be shut down afterward.' if force_restart else \
        'Please restart the kernel once the packages have been upgraded.'
    status.update(f'Running "{pip_command}". {restart_message}', Status.RUNNING)
    ipython.run_cell(pip_command)

    if force_restart:
        if not ipython.kernel:
            raise SPyValueError(f'Unable get IPython kernel to complete restart')
        ipython.kernel.do_shutdown(True)
