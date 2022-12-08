# =============================================================================
# Docdocdoc Utilities
# =============================================================================
#
# Miscellaneous utility functions used throughout the library.
#
import re

MULTIPLE_LINE_BREAK_RE = re.compile(r"\n\n\n+")

MULTIPLE_RE = re.compile(r"([^a-zA-Z0-9#*/_\-\n])\1+")


def collapse(text):
    return text.replace("\n", " ").strip()


def clean_line_break(text):
    return MULTIPLE_LINE_BREAK_RE.sub("\n\n", text)


def clean_multiple(text):
    return MULTIPLE_RE.sub(r"\1", text)
