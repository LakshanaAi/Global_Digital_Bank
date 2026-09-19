from gdb.domain.account import Account


class SavingsAccount(Account):

    def __init__(
        self,
        account_number: str,
        age: int,
        initial_balance: float,
        pin: str,
        interest_rate: float
    ):
        super().__init__(
            account_number=account_number,
            age=age,
            initial_balance=initial_balance,
            pin=pin,
            account_type="Savings"
        )

        self._interest_rate = interest_rate

    def calculate_interest(self) -> float:
        return self._balance * self._interest_rate / 100