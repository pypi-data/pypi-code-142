class PointerString:
    _string: str
    _pointer: int

    @property
    def pointer(self) -> int:
        return self._pointer
    
    @pointer.setter
    def pointer(self, value: int) -> None:
        self._check_if_value_is_correct_pointer_and_raise_error_if_not(value)
        self._pointer = value

    @property
    def string(self) -> str:
        return self._string

    def __init__(self, string):
        self._string = string
        self.pointer = 0

    def _check_if_value_is_correct_pointer_and_raise_error_if_not(self, value):
        if not (0 <= value < len(self._string)):
            raise IndexError("pointer out of the string")

    def move(self, steps: int) -> str:
        new: int = self.pointer + steps
        self.pointer = new
        return self.get_symb()
    
    def get_symb(self, offset: int = 0) -> str:
        index: int = self.pointer+offset
        self._check_if_value_is_correct_pointer_and_raise_error_if_not(index)
        return self._string[index]

    def __len__(self): 
        return len(self._string)
    
    def __copy__(self):
        new: PointerString = PointerString(self._string)
        new.pointer = self.pointer
        return new