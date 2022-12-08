from typing import Dict

from .pattern_filter import PatternFilter


class Phone(PatternFilter):
    name: str = "PHONE"

    patterns: Dict[str, str] = {"landline_es": r"\+\d{11}"}
