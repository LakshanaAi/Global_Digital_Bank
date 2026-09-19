from abc import ABC, abstractmethod


class IAccount(ABC):

    @property
    @abstractmethod
    def account_number(self) -> str:
        pass

    @property
    @abstractmethod
    def balance(self) -> float:
        pass

    @abstractmethod
    def deposit(self, amount: float) -> bool:
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> bool:
        pass

    @abstractmethod
    def calculate_interest(self) -> float:
        pass

    @abstractmethod
    def get_account_type(self) -> str:
        pass