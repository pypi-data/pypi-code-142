from typing import Tuple, List, Any, Dict

from .excel import ExcelCoverLetterManager
from .models import CoverLetter
from .sqlite import CoverLetterManager
from ..enums import FilterType
from ..exceptions import CoverLetterException  # type: ignore
from ..utils import backup_excel  # type: ignore


def synchronize_to_excel(excel_manager: ExcelCoverLetterManager, db_manager: CoverLetterManager,
                         all_cover_letters: bool = False):
    backup_file = None
    cover_letter_xlsx = excel_manager.filename
    if cover_letter_xlsx.exists():
        backup_file = backup_excel(cover_letter_xlsx)
        if not backup_file.exists():
            error_message = f'Backup file was not created. Cannot overwrite {cover_letter_xlsx}'
            raise CoverLetterException(error_message)
    cover_letter_xlsx.unlink(missing_ok=True)
    if all_cover_letters:
        cover_letters = db_manager.list()
    else:
        cover_letters = db_manager.filter(FilterType.COVER_LETTER_NOT_DELETED)
    excel_manager.write_template()
    excel_manager.add(cover_letters)
    return backup_file, len(cover_letters)


def synchronize_to_db(excel_manager: ExcelCoverLetterManager, db_manager: CoverLetterManager,
                      delete: bool = False) -> Tuple[List[CoverLetter], List[CoverLetter],
                                                     List[CoverLetter], List[Dict[str, Any]]]:
    excel_cover_letters = excel_manager.read()
    updated_list = list()
    deleted_list = list()
    created_list = list()
    errors_list = list()
    for cover_letter in excel_cover_letters:
        if cover_letter.id is None:
            db_manager.create(cover_letter)
            created_list.append(cover_letter)
        else:
            db_cover_letter = db_manager.get(cover_letter.id)
            if db_cover_letter is None:
                errors_list.append({'error': 'Not found', 'cover_letter': cover_letter.dict()})
            else:
                if db_cover_letter != cover_letter:
                    if delete and db_cover_letter.delete:
                        db_manager.delete(cover_letter)
                        deleted_list.append(cover_letter)
                    else:
                        db_manager.update(cover_letter)
                        updated_list.append(cover_letter)
    return created_list, updated_list, deleted_list, errors_list
