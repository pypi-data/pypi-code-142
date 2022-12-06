from unittest import mock

import pytest

from seeq import spy
from seeq.spy import Session
from seeq.spy._errors import SPyValueError


@pytest.mark.unit
def test_upgrade():
    mock_session = mock.Mock(Session)
    mock_session.client = {}

    def _override_get_server_version_tuple(session):
        return 123, 456, 789

    def _override_is_ipython():
        return True

    def _override_is_ipython_interactive():
        return True

    mock_kernel = mock.Mock()
    mock_ipython = mock.Mock()
    mock_ipython.kernel = mock_kernel

    def _override_get_ipython():
        return mock_ipython

    with mock.patch('seeq.spy._login.get_server_version_tuple', _override_get_server_version_tuple), \
            mock.patch('seeq.spy._datalab.is_ipython', _override_is_ipython), \
            mock.patch('seeq.spy._datalab.is_ipython_interactive', _override_is_ipython_interactive), \
            mock.patch('IPython.get_ipython', _override_get_ipython):
        # Default upgrade should request major and minor Server version
        spy.upgrade(session=mock_session)
        mock_ipython.run_cell.assert_called_with('pip install -U seeq~=123.456')
        assert not mock_kernel.do_shutdown.called

        # Upgrade can specify a particular version, removing the 'R' if needed. Expect `==` to be used.
        spy.upgrade(version='R60.0.1.184.15', session=mock_session, force_restart=True)
        mock_ipython.run_cell.assert_called_with('pip install -U seeq==60.0.1.184.15')
        mock_kernel.do_shutdown.assert_called_with(True)

    # Error expected if not in IPython
    with mock.patch('seeq.spy._login.get_server_version_tuple', _override_get_server_version_tuple), \
            mock.patch('seeq.spy._datalab.is_ipython_interactive', _override_is_ipython_interactive), \
            mock.patch('IPython.get_ipython', _override_get_ipython):
        with pytest.raises(SPyValueError, match='must be invoked from a Jupyter notebook'):
            spy.upgrade(session=mock_session)

    # Error expected if not in a Jupyter notebook
    with mock.patch('seeq.spy._login.get_server_version_tuple', _override_get_server_version_tuple), \
            mock.patch('seeq.spy._datalab.is_ipython', _override_is_ipython), \
            mock.patch('IPython.get_ipython', _override_get_ipython):
        with pytest.raises(SPyValueError, match='must be invoked from a Jupyter notebook'):
            spy.upgrade(session=mock_session)

    # Error expected if not able to get IPython instance
    with mock.patch('seeq.spy._login.get_server_version_tuple', _override_get_server_version_tuple), \
            mock.patch('seeq.spy._datalab.is_ipython', _override_is_ipython), \
            mock.patch('seeq.spy._datalab.is_ipython_interactive', _override_is_ipython_interactive):
        with pytest.raises(SPyValueError, match='must be invoked from a Jupyter notebook'):
            spy.upgrade(session=mock_session)

    # Error expected if not able to get kernel for restart
    mock_ipython.kernel = None
    with mock.patch('seeq.spy._login.get_server_version_tuple', _override_get_server_version_tuple), \
            mock.patch('seeq.spy._datalab.is_ipython', _override_is_ipython), \
            mock.patch('seeq.spy._datalab.is_ipython_interactive', _override_is_ipython_interactive), \
            mock.patch('IPython.get_ipython', _override_get_ipython):
        with pytest.raises(SPyValueError, match='Unable get IPython kernel to complete restart'):
            spy.upgrade(session=mock_session, force_restart=True)
