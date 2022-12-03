from py_cover_letters.db.excel import ExcelCoverLetterManager
from py_cover_letters.constants import COLUMN_MAPPING
from tests.factories import CoverLetterFactory
from tests.utils import read_excel


class TestExcelCoverManager:

    def test_write_template(self, output_folder):
        filename = output_folder / 'sample_cover_letter.xlsx'
        filename.unlink(missing_ok=True)
        manager = ExcelCoverLetterManager(filename, column_mapping=COLUMN_MAPPING)

        manager.write_template()
        assert filename.exists()
        excel_content = read_excel(filename, 'Cover letters', column_mapping=COLUMN_MAPPING,
                                   include_headers=True)
        expected_columns = {'company_name', 'cover_template', 'date_generated', 'date_sent_via_email', 'delete',
                            'greeting', 'id', 'position_name', 'to_email'}
        assert len(excel_content) == 1
        assert set(excel_content[0].keys()) == expected_columns

    def test_add(self, output_folder):
        filename = output_folder / 'sample_cover_letter.xlsx'
        filename.unlink(missing_ok=True)
        excel_manager = ExcelCoverLetterManager(filename, column_mapping=COLUMN_MAPPING)

        excel_manager.write_template()
        assert filename.exists()
        cover_letters = CoverLetterFactory.create_batch(5)
        excel_manager.add(cover_letters)

        read_cl = excel_manager.read()
        assert len(read_cl) == 5
