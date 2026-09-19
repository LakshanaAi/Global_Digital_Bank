from gdb.exceptions.account_exception import AccountException


class MinimumBalanceViolationException(AccountException):
    """Raised when a transaction violates the minimum balance requirement."""
    pass