from gdb.exceptions.account_exception import AccountException


class InactiveAccountException(AccountException):
    """Raised when an operation is attempted on an inactive account."""
    pass