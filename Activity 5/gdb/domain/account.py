from gdb.exceptions.account_exception import AccountException
from gdb.exceptions.invalid_amount_exception import InvalidAmountException
from gdb.exceptions.insufficient_balance_exception import InsufficientBalanceException
from gdb.exceptions.inactive_account_exception import InactiveAccountException
from gdb.exceptions.invalid_pin_exception import InvalidPinException
from gdb.exceptions.minimum_balance_violation_exception import (
    MinimumBalanceViolationException
)


class Account:

    MINIMUM_BALANCE = 0.0

    def __init__(
        self,
        account_number: str,
        age: int,
        initial_balance: float,
        pin: str
    ):
        # Account number validation
        if not account_number:
            raise AccountException("Account number cannot be empty.")

        # Age validation
        if age < 18:
            raise AccountException(
                "Customer must be at least 18 years old."
            )

        # Initial balance validation
        if initial_balance < 0:
            raise InvalidAmountException(
                "Initial balance cannot be negative."
            )

        # PIN validation
        if (
            not isinstance(pin, str)
            or not pin.isdigit()
            or len(pin) != 4
        ):
            raise InvalidPinException(
                "PIN must be exactly 4 digits."
            )

        self._account_number = account_number
        self._age = age
        self._balance = initial_balance
        self._pin = pin
        self._status = "ACTIVE"

    def get_balance(self):
        return self._balance

    def get_status(self):
        return self._status

    def validate_pin(self, entered_pin: str) -> bool:

        if entered_pin is None or entered_pin != self._pin:
            raise InvalidPinException(
                "Invalid PIN."
            )

        return True

    def deposit(self, amount: float) -> bool:

        # Check account status
        if self._status.lower() != "active":
            raise InactiveAccountException(
                "Account is not active."
            )

        # Check amount
        if amount <= 0:
            raise InvalidAmountException(
                "Deposit amount must be greater than zero."
            )

        self._balance += amount
        return True

    def withdraw(self, amount: float, entered_pin: str) -> bool:

        # Check account status
        if self._status.lower() != "active":
            raise InactiveAccountException(
                "Account is not active."
            )

        # Validate PIN
        self.validate_pin(entered_pin)

        # Check amount
        if amount <= 0:
            raise InvalidAmountException(
                "Withdrawal amount must be greater than zero."
            )

        # Check balance
        if amount > self._balance:
            raise InsufficientBalanceException(
                "Insufficient balance."
            )

        # Minimum balance check
        if self._balance - amount < self.MINIMUM_BALANCE:
            raise MinimumBalanceViolationException(
                "Withdrawal would violate the minimum balance requirement."
            )

        self._balance -= amount
        return True

    def suspend(self):
        self._status = "SUSPENDED"

    def activate(self):
        self._status = "ACTIVE"

    def close(self):
        self._status = "CLOSED"