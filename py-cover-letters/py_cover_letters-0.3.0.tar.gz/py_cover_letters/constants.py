from pathlib import Path

from py_cover_letters import CURRENT_CONFIGURATION

BANNER = """
*******************************************************************************
******************************* PY-COVER-LETTERS **************************
*******************************************************************************
"""  # noqa
COLUMN_MAPPING = {
    1: 'id',
    2: 'company_name',
    3: 'position_name',
    4: 'greeting',
    5: 'to_email',
    6: 'cover_template',
    7: 'date_sent_via_email',
    8: 'date_generated',
    9: 'delete'
}
SHEET_NAME = 'Cover letters'
SQLITE_FILENAME = 'cover_letters.sqlite'
SQLITE_FILE = Path(CURRENT_CONFIGURATION['database']['folder']) / SQLITE_FILENAME
EXCEL_FILE = Path(CURRENT_CONFIGURATION['database']['folder']) / CURRENT_CONFIGURATION['database']['file']
DEFAULT_OUTPUT_FOLDER = Path(CURRENT_CONFIGURATION['cover_letters']['default_output_folder'])
DEFAULT_TEMPLATE = Path(CURRENT_CONFIGURATION['cover_letters']['template_folder']) / \
                   CURRENT_CONFIGURATION['cover_letters']['default_template']
DEFAULT_DB_BACKUP_FOLDER = Path(CURRENT_CONFIGURATION['database']['backup_folder'])
