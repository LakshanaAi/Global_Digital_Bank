from gdb.exceptions.account_exception import AccountException


class InsufficientBalanceException(AccountException):
    """Raised when withdrawal exceeds available balance."""
    pass