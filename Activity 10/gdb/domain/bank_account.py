from abc import ABC, abstractmethod


class BankAccount(ABC):

    def __init__(
        self,
        account_number: str,
        balance: float
    ):
        self._account_number = account_number
        self._balance = balance

    @abstractmethod
    def calculate_interest(self) -> float:
        pass

    @abstractmethod
    def get_account_type(self) -> str:
        pass

    def display_account_info(self):
        print("Account Number:", self._account_number)
        print("Account Type:", self.get_account_type())
        print("Balance: Rs", self._balance)
        print("Interest: Rs", self.calculate_interest())