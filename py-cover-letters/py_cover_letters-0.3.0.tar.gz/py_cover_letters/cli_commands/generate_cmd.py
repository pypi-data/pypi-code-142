from pathlib import Path
from typing import Any, List, Dict, Optional

from ..constants import DEFAULT_OUTPUT_FOLDER, DEFAULT_TEMPLATE
from ..db.managers import ExcelManager
from ..enums import FilterType
from ..generators import build_cover_letter_filename, write_docx_cover_letter, convert_docx_to_pdf
from ..utils import is_libreoffice_installed


def do_generate(excel_file: Path, template: Optional[Path] = None) -> List[Dict[str, Any]]:
    if template is None:
        template = DEFAULT_TEMPLATE
    excel_manager = ExcelManager(excel_file)
    not_created = excel_manager.filter(FilterType.COVER_LETTER_NOT_CREATED)
    generated = list()
    for cover_letter in not_created:
        data = {'cover_letter': cover_letter.dict()}
        ctx = cover_letter.get_context()
        cover_letter_file = build_cover_letter_filename(DEFAULT_OUTPUT_FOLDER, ctx)
        write_docx_cover_letter(template, ctx, cover_letter_file)
        data['docx'] = cover_letter_file
        data['pdf'] = {'file': None, 'errors': ['Libreoffice not installed']}
        if is_libreoffice_installed():
            pdf, errors_list = convert_docx_to_pdf(cover_letter_file)
            data['pdf'] = {'file': pdf, 'errors': errors_list}

        generated.append(data)
    return generated
