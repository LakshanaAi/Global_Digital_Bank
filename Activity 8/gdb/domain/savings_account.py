from gdb.domain.account import Account
from gdb.exceptions.minimum_balance_violation_exception import (
    MinimumBalanceViolationException
)


class SavingsAccount(Account):

    MINIMUM_BALANCE = 1000.0

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

    def withdraw(self, amount: float, entered_pin: str) -> bool:

        # Validate account status
        if self._status.lower() != "active":
            from gdb.exceptions.inactive_account_exception import (
                InactiveAccountException
            )
            raise InactiveAccountException(
                "Account is not active."
            )

        # Validate PIN
        self.validate_pin(entered_pin)

        # Validate amount
        if amount <= 0:
            from gdb.exceptions.invalid_amount_exception import (
                InvalidAmountException
            )
            raise InvalidAmountException(
                "Withdrawal amount must be greater than zero."
            )

        # Check sufficient balance
        if amount > self._balance:
            from gdb.exceptions.insufficient_balance_exception import (
                InsufficientBalanceException
            )
            raise InsufficientBalanceException(
                "Insufficient balance."
            )

        # Savings-specific minimum balance check
        if self._balance - amount < self.MINIMUM_BALANCE:
            raise MinimumBalanceViolationException(
                "Savings account must maintain a minimum balance of Rs 1000."
            )

        self._balance -= amount
        return True