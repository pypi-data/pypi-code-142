import re
from datetime import datetime

from py_cover_letters.generators import write_docx_cover_letter, convert_docx_to_pdf
from py_cover_letters.utils import get_libreoffice_version
from tests.conftest import libreoffice_required


@libreoffice_required
def test_get_libreoffice_version():
    regexp = re.compile(r"(\d\.\d\.\d\.?\d?)\s?(\d*)\(Build:\d+\)")
    version, is_valid = get_libreoffice_version()
    assert regexp.match(version) is not None
    assert is_valid


def test_write_cover_letter(fixtures_folder, output_folder):
    template = fixtures_folder / 'templates' / 'Cover Letter Template.docx'
    assert template.exists()
    today = datetime.today()
    context = {'date': today.strftime('%b %M %Y'), 'position_name': 'Jedi Knight',
               'company_name': 'Jedi Order Council'}

    docx_filename = f'{today.strftime("%Y%m%d")}_cover_{context["company_name"]}_{context["position_name"]}.docx'
    cover_letter = output_folder / docx_filename
    cover_letter.unlink(missing_ok=True)

    write_docx_cover_letter(template, context, cover_letter)
    assert cover_letter.exists()


# @libreoffice_required
def test_convert_docx_to_pdf(docx_template_file, output_folder):
    today = datetime.today()
    context = {'date': today.strftime('%B %-d, %Y'), 'position_name': 'Jedi Knight',
               'company_name': 'Jedi Order Council'}
    naming_context = context  # humps.camelize(context)
    docx_filename = f'{today.strftime("%Y%m%d")}_cover_{naming_context["company_name"]}' \
                    f'_{naming_context["position_name"]}.docx'
    cover_letter = output_folder / docx_filename
    cover_letter.unlink(missing_ok=True)

    write_docx_cover_letter(docx_template_file, context, cover_letter)
    assert cover_letter.exists()

    pdf, errors = convert_docx_to_pdf(cover_letter, output_folder)
    assert pdf.exists()
    assert len(errors) == 1
    pdf.unlink(missing_ok=True)


def test_convert_docx_to_pdf_invalid(fixtures_folder, output_folder):
    txt_file = fixtures_folder / 'template' / 'email_static_txt.txt'
    pdf, errors = convert_docx_to_pdf(txt_file, output_folder)
    assert pdf is None
    assert len(errors) == 3
