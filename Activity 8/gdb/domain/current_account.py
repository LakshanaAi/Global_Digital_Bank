from gdb.domain.account import Account
from gdb.exceptions.insufficient_balance_exception import (
    InsufficientBalanceException
)
from gdb.exceptions.inactive_account_exception import (
    InactiveAccountException
)
from gdb.exceptions.invalid_amount_exception import (
    InvalidAmountException
)


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

    def withdraw(self, amount: float, entered_pin: str) -> bool:

        # Check account status
        if self._status.lower() != "active":
            raise InactiveAccountException(
                "Account is not active."
            )

        # Validate PIN
        self.validate_pin(entered_pin)

        # Validate amount
        if amount <= 0:
            raise InvalidAmountException(
                "Withdrawal amount must be greater than zero."
            )

        # Maximum amount that can be withdrawn
        available_amount = self._balance + self._overdraft_limit

        if amount > available_amount:
            raise InsufficientBalanceException(
                "Withdrawal exceeds balance and overdraft limit."
            )

        self._balance -= amount
        return True