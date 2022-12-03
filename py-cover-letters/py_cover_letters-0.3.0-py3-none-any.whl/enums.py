from enum import Enum


class FilterType(int, Enum):
    COVER_LETTER_CREATED = 0
    COVER_LETTER_NOT_CREATED = 1
    COVER_LETTER_SENT = 2
    COVER_LETTER_NOT_SENT = 3
    COVER_LETTER_NOT_DELETED = 4
