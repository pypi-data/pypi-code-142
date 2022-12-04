from typing import Union

class Operation:
    def __init__(
        self, first_number: Union[float,int], 
        second_number: Union[float,int]
    ) -> None:
        self.first_number = first_number
        self.second_number = second_number
    
    def addition(self) -> Union[float,int]:
        return self.first_number + self.second_number
    
    def subtraction(self) -> Union[float,int]:
        return self.first_number - self.second_number
        
    def multiplication(self) -> Union[float,int]:
        return self.first_number * self.second_number
        
    def division(self) -> Union[float,int]:
        return self.first_number / self.second_number