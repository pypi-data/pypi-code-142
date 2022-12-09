from abc import ABC, abstractmethod


class POS(ABC):

    @abstractmethod
    def sign_in(self, device: str, merchant: str) -> None:
        pass

    @abstractmethod
    def sign_out(self, device: str) -> None:
        pass

    @abstractmethod
    def query(self, device: str) -> dict:
        pass

    @abstractmethod
    def pay(self, device: str, amount: int) -> dict:
        pass
