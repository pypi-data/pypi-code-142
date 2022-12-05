from dataclasses import dataclass

from palign.style import Style


@dataclass
class TextLineCharacter:
    """
    Describes the render coordinates of a character.
    """

    character: str
    """
    Character.
    """

    style: Style
    """
    Character style.
    """

    x: float
    """
    X pixel coordinate.
    """
