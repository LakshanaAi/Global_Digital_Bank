from gdb.domain.iaccount import IAccount


class AbstractAccount(IAccount):

    def __init__(self, account_number: str, balance: float):
        self._account_number = account_number
        self._balance = balance

    @property
    def account_number(self) -> str:
        return self._account_number

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            return False

        self._balance += amount
        return True

    def withdraw(self, amount: float) -> bool:
        if amount <= 0 or amount > self._balance:
            return False

        self._balance -= amount
        return True

    def calculate_interest(self) -> float:
        return 0.0

    def get_account_type(self) -> str:
        return "Abstract"