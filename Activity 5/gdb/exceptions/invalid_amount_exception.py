from gdb.exceptions.account_exception import AccountException


class InvalidAmountException(AccountException):
    """Raised when an amount is zero or negative."""
    pass