from gdb.domain.account import Account


class CurrentAccount(Account):

    def __init__(
        self,
        account_number: str,
        age: int,
        initial_balance: float,
        pin: str,
        overdraft_limit: float
    ):
        super().__init__(
            account_number=account_number,
            age=age,
            initial_balance=initial_balance,
            pin=pin,
            account_type="Current"
        )

        self._overdraft_limit = overdraft_limit