import pytest
import os

from src.mytypo import check_typo
# this comment has miss spel word

def test_typo_correction():
    p = os.path.abspath(".") + "/tests/test_mytypo.py"
    suggestions = check_typo(path=p)
    assert len(suggestions) == 1
