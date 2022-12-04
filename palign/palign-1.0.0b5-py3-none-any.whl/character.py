from dataclasses import dataclass


@dataclass
class TextLineCharacter:
    """
    Describes the render coordinates of a character.
    """

    character: str
    """
    Character.
    """

    x: float
    """
    X pixel coordinate.
    """
