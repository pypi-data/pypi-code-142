import shutil
from pathlib import Path

import pytest

from py_cover_letters.db.sqlite import CoverLetterManager
from py_cover_letters.utils import is_libreoffice_installed
from tests.factories import CoverLetterFactory


@pytest.fixture(scope='session')
def output_folder():
    folder = Path(__file__).parent.parent / 'output'
    folder.mkdir(exist_ok=True)
    return folder


@pytest.fixture(scope='session')
def fixtures_folder():
    folder = Path(__file__).parent.parent / 'tests' / 'fixtures'
    return folder


@pytest.fixture(scope='session')
def docx_template_file(fixtures_folder):
    template = fixtures_folder / 'templates' / 'Cover Letter Template.docx'
    return template


@pytest.fixture(scope='function')
def testing_database_file(output_folder):
    filename = output_folder / 'test_cover_letters.sqlite'
    yield filename
    filename.unlink(missing_ok=True)


@pytest.fixture(scope='function')
def excel_file(output_folder):
    filename = output_folder / 'test_cover_letters.xlsx'
    yield filename
    filename.unlink(missing_ok=True)


@pytest.fixture(scope='function')
def cover_letter_manager(testing_database_file) -> CoverLetterManager:
    cover_letters = CoverLetterFactory.create_batch(5, id=None)
    cover_letters.extend(CoverLetterFactory.create_batch(6, new=True))
    cover_letters.extend(CoverLetterFactory.create_batch(2, new=True, delete=True))
    db_manager = CoverLetterManager(testing_database_file)
    for cover_letter in cover_letters:
        db_manager.create(cover_letter)
    return db_manager


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


@pytest.fixture(scope='function')
def excel_file_without_id(output_folder, fixtures_folder):
    excel_without_id = fixtures_folder / 'test_cover_letters_without_ids.xlsx'
    # timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    timestamp = next(infinite_sequence())
    excel_file = output_folder / f'{timestamp:03d}_test_cover_letters_without_ids.xlsx'
    shutil.copy(excel_without_id, excel_file)
    return excel_file


@pytest.fixture(scope='function')
def short_excel_file_without_id(output_folder, fixtures_folder):
    excel_without_id = fixtures_folder / 'test_short_cover_letters_without_ids.xlsx'
    # timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    timestamp = next(infinite_sequence())
    excel_file = output_folder / f'{timestamp:03d}_test_cover_letters_without_ids.xlsx'
    shutil.copy(excel_without_id, excel_file)
    return excel_file


libreoffice_required = pytest.mark.skipif(
    is_libreoffice_installed, reason="Libre office is required to run."
)
