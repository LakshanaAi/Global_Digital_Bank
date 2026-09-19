from gdb.domain.bank_account import BankAccount


class SavingsAccount(BankAccount):

    def __init__(
        self,
        account_number: str,
        balance: float,
        interest_rate: float
    ):
        super().__init__(account_number, balance)
        self._interest_rate = interest_rate

    def calculate_interest(self) -> float:
        return self._balance * self._interest_rate / 100

    def get_account_type(self) -> str:
        return "Savings"