from typing import Union

__all__ = ["Plural", "possessive"]


class Plural:
    def __init__(self, num: Union[int, float]):
        """Returns the plural version of the given text

        Parameters
        ----------
        num: Union[`int`, `float`]
            the number you want to use for getting the plural of text

        Useage
        ----------
        Example: `Plural(5):the_text` -> `5 the_texts`
        """

        self.num = num

    def __format__(self, text: str) -> str:
        if abs(self.num) != 1:
            text += "s"

        return f"{self.num} {text}"


def possessive(text: str) -> str:
    """Returns the possessive version of the given text

    Parameters
    ----------
    text: `str`
        The text you want the possessive version of

    Returns
    ----------
    str
        The possessive version of the text
    """

    if text.endswith("s"):
        text += "'"
    else:
        text += "'s"

    return text
