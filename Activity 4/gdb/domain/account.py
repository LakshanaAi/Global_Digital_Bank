class Account:
    def __init__(
        self,
        account_number: str,
        age: int,
        initial_balance: float,
        pin: str
    ):
        # Validate account number
        if not account_number:
            raise ValueError("Account number cannot be empty")

        # Validate age
        if age < 18:
            raise ValueError("Customer must be at least 18 years old")

        # Validate initial balance
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")

        # Validate PIN
        if not isinstance(pin, str) or not pin.isdigit() or len(pin) != 4:
            raise ValueError("PIN must be exactly 4 digits")

        # Assign values
        self._account_number = account_number
        self._age = age
        self._balance = initial_balance
        self._pin = pin
        self._status = "ACTIVE"

    def get_balance(self) -> float:
        return self._balance

    def get_account_number(self) -> str:
        return self._account_number

    def get_status(self) -> str:
        return self._status

    def validate_pin(self, entered_pin: str) -> bool:
        if entered_pin is None:
            return False

        return entered_pin == self._pin

    def deposit(self, amount: float) -> bool:
        # Account must be active
        if self._status.lower() != "active":
            return False

        # Amount must be positive
        if amount <= 0:
            return False

        self._balance += amount
        return True

    def withdraw(self, amount: float, entered_pin: str) -> bool:
        # Account must be active
        if self._status.lower() != "active":
            return False

        # PIN must be correct
        if not self.validate_pin(entered_pin):
            return False

        # Amount must be positive
        if amount <= 0:
            return False

        # Cannot withdraw more than balance
        if amount > self._balance:
            return False

        self._balance -= amount
        return True

    def suspend(self):
        self._status = "SUSPENDED"

    def activate(self):
        self._status = "ACTIVE"

    def close(self):
        self._status = "CLOSED"