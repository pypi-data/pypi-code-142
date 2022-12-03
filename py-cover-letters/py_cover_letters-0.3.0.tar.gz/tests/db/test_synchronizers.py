from py_cover_letters.constants import COLUMN_MAPPING
from py_cover_letters.db.excel import ExcelCoverLetterManager, excel_to_list
from py_cover_letters.db.sqlite import CoverLetterManager
from py_cover_letters.db.synchronizers import synchronize_to_db, synchronize_to_excel
from tests.factories import CoverLetterFactory


def test_synchronize_to_db(output_folder, testing_database_file):
    filename = output_folder / 'sample_cover_letter.xlsx'
    filename.unlink(missing_ok=True)
    excel_manager = ExcelCoverLetterManager(filename, column_mapping=COLUMN_MAPPING)

    excel_manager.write_template()
    assert filename.exists()
    cover_letters = CoverLetterFactory.create_batch(5, new=True)
    excel_manager.add(cover_letters)

    manager = CoverLetterManager(testing_database_file)
    results = synchronize_to_db(excel_manager, manager)

    assert len(results[0]) == 5
    assert len(results[1]) == 0
    assert len(results[2]) == 0


def test_synchronize_to_excel(cover_letter_manager, excel_file):
    excel_manager = ExcelCoverLetterManager(excel_file, column_mapping=COLUMN_MAPPING)
    excel_manager.filename.unlink(missing_ok=True)
    excel_manager.write_template()
    backup_filename, count = synchronize_to_excel(excel_manager, cover_letter_manager)
    assert backup_filename.exists()
    assert count == 11

    cover_letter_list = excel_to_list(excel_file, 'Cover letters', COLUMN_MAPPING)
    assert len(cover_letter_list) == 11


def test_synchronize_to_db_from_file_without_ids(fixtures_folder, testing_database_file):
    excel_file = fixtures_folder / 'test_cover_letters_without_ids.xlsx'
    excel_manager = ExcelCoverLetterManager(excel_file)
    content = excel_manager.read()  # read_excel(excel_file)
    assert len(content) == 50

    db_manager = CoverLetterManager(testing_database_file)
    db_content = db_manager.list()
    assert len(db_content) == 0

    synchronize_to_db(excel_manager, db_manager)
    db_content = db_manager.list()
    assert len(db_content) == 50
