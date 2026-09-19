from gdb.exceptions.account_exception import AccountException


class InvalidPinException(AccountException):
    """Raised when an invalid PIN is provided."""
    pass