from typing import Dict
from .pattern_filter import PatternFilter


class Email(PatternFilter):
    name: str = "EMAIL"

    patterns: Dict[str, str] = {"email": r"[a-zA-Z0-9\.]+@[a-zA-Z]+.[a-zA-Z]{1,3}"}
