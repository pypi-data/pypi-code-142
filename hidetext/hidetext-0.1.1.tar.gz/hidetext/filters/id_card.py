from typing import Dict

from .pattern_filter import PatternFilter


class IdCard(PatternFilter):
    name: str = "ID_CARD"

    patterns: Dict[str, str] = {
        "dni": r"\d{8}[A-Z]",
        "nie": r"[X,Y,Z]\d{7}[A-Z]",
    }
