import re


class PolishNoteNamesPreprocessor:
    @classmethod
    def process(cls, raw: str) -> str:
        product = re.sub(r"\[B", "[Bb", raw, flags=re.IGNORECASE)
        product = re.sub(r"\[H", "[B", product, flags=re.IGNORECASE)
        return product
