from typing import Optional


class Response:
    def __init__(
        self,
        status: int,
        content_type: Optional[str] = None,
        text: Optional[str] = None,
    ):
        self.status = status
        self.text = text
        self.content_type = content_type

    def is_html(self) -> bool:
        return not self.content_type or any(
            mime_type in self.content_type
            for mime_type in ["text/html", "application/xhtml+xml"]
        )

    def ok(self) -> bool:
        return self.status < 400
