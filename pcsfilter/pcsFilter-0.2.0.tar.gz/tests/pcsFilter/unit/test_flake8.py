from pathlib import Path

import pytest  # noqa

from src.pcsFilter.file_handling.file_finder import find_file
from src.pcsFilter.tools.flake8 import run_flake8
from tests.pcsFilter.unit.fixtures import create_temp_file  # noqa


@pytest.mark.parametrize(
    "create_temp_file",
    [{"file_name": "temp_test_flake8.py", "file_content": "\nimport os"}],
    indirect=True,
)
@pytest.mark.unit
def test_flake8(create_temp_file):
    """Test that flake8 is launched"""
    error1 = "F401 'os' imported but unused"
    error2 = "W292 no newline at end of file"
    path = create_temp_file.name()
    output_path = Path('.')

    run_flake8(path=path, output_path=output_path)

    file_handler = find_file("flake8.txt")
    actual_content = file_handler.get_content()
    file_handler.delete()

    assert error1 in actual_content
    assert error2 in actual_content
