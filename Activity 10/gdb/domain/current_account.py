from gdb.domain.bank_account import BankAccount


class CurrentAccount(BankAccount):

    def __init__(
        self,
        account_number: str,
        balance: float
    ):
        super().__init__(account_number, balance)

    def calculate_interest(self) -> float:
        return 0.0

    def get_account_type(self) -> str:
        return "Current"