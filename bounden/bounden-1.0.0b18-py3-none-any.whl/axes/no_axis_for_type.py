from typing import Any


class NoAxisForType(ValueError):
    """
    Raised when an axis cannot be found to handle axis `value`.
    """

    def __init__(self, value: Any) -> None:
        msg = f"No axis for {repr(value)} ({value.__class__.__name__})"
        super().__init__(msg)
