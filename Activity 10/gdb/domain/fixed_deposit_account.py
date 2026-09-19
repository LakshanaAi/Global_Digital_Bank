from gdb.domain.bank_account import BankAccount


class FixedDepositAccount(BankAccount):

    def __init__(
        self,
        account_number: str,
        balance: float,
        interest_rate: float,
        tenure_years: int
    ):
        super().__init__(account_number, balance)

        self._interest_rate = interest_rate
        self._tenure_years = tenure_years

    def calculate_interest(self) -> float:
        return (
            self._balance
            * self._interest_rate
            * self._tenure_years
            / 100
        )

    def get_account_type(self) -> str:
        return "Fixed Deposit"