import dataclasses
from typing import Dict, Literal
from urllib.parse import urlencode, quote

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types
# https://en.wikipedia.org/wiki/Media_type
Mimetype = Literal[
    'text/plain',
    'text/html',
    'text/csv',
    'application/json',
    'application/pdf',
    'application/zip',
    'application/octet-stream',
        # .docx
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        # .xlsx
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
]


@dataclasses.dataclass
class ContentDisposition:
    filename: str
    content_type: Mimetype = 'application/octet-stream'

    @classmethod
    def docx(cls, filename):
        return cls(filename, "application/vnd.openxmlformats-officedocument.wordprocessingml.document")

    @classmethod
    def xlsx(cls, filename):
        return cls(filename, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    @classmethod
    def pdf(cls, filename):
        return cls(filename, "application/pdf")

    @property
    def filename_encoded(self) -> str:
        """
        >>> ContentDisposition.xlsx('Отчет.xlsx').filename_encoded
        'filename=%D0%9E%D1%82%D1%87%D0%B5%D1%82.xlsx'
        """
        return urlencode({"filename": self.filename}, quote_via=quote)

    @property
    def header(self) -> str:
        """
        >>> ContentDisposition.xlsx('report.xlsx').header
        'attachment; filename=report.xlsx'
        """
        return f'attachment; {self.filename_encoded}'

    @property
    def header_dict(self) -> Dict[str, str]:
        """
        >>> ContentDisposition.xlsx('report.xlsx').header_dict
        {'Content-Disposition': 'attachment; filename=report.xlsx'}
        """
        return {'Content-Disposition': self.header}
