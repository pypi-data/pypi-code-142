import pytest  # noqa

from src.pcsFilter.file_handling.abstract_file_handler import AFileHandler
from src.pcsFilter.file_handling.file_finder import find_file


@pytest.fixture
def create_temp_file(request) -> AFileHandler:
    """Create temporary test file"""
    temp_file = find_file(request.param["file_name"]).write(
        request.param["file_content"]
    )

    yield temp_file

    temp_file.delete()


@pytest.fixture
def roll_back_file(request) -> None:
    """Read file content before the test
    and roll it back after"""
    updatable_file = find_file(request.param)
    initial_content = updatable_file.get_content()

    yield

    updatable_file.write(initial_content)
