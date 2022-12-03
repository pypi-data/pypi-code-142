from py_cover_letters.utils import get_libreoffice_version


def test_get_libreoffice_version_not_found(mocker):
    mock = mocker.patch('py_cover_letters.utils.run_commands', return_value=([], []))
    version, is_valid = get_libreoffice_version()
    assert version == 'Libreoffice not found.'
    assert not is_valid
    mock.called_once()


def test_get_libreoffice_version(mocker):
    mock = mocker.patch('py_cover_letters.utils.run_commands',
                        return_value=(['LibreOffice 7.3.6.2 30(Build:2)'], []))
    version, is_valid = get_libreoffice_version()
    assert version == '7.3.6.2 30(Build:2)'
    assert is_valid
    mock.called_once()
